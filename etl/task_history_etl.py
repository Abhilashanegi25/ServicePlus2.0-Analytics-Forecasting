from sqlalchemy import create_engine
import pandas as pd
from db_config import DATABASE_URL

# -------------------------
# DATABASE CONNECTION
# -------------------------

engine = create_engine(DATABASE_URL)

# -------------------------
# EXTRACT DATA
# -------------------------

query = """
SELECT
    application_id,
    appl_status,
    execution_data
FROM data_stats
WHERE execution_data IS NOT NULL
AND appl_status IN ('F','D','R')
"""

df = pd.read_sql(query, engine)

print("Applications loaded:", len(df))

# -------------------------
# BUILD FACT TASK HISTORY
# -------------------------

records = []

task_history_key = 1

for _, row in df.iterrows():

    application_id = row["application_id"]
    appl_status = row["appl_status"]
    execution_data = row["execution_data"]

    if execution_data is None:
        continue

    try:

        for task_group in execution_data:

            if not task_group:
                continue

            for task_record in task_group:

                task_info = task_record.get("task_info", {})

                user_detail = task_info.get("user_detail")

                if user_detail is None:
                    user_detail = {}

                received_time = pd.to_datetime(
                    task_info.get("received_time"),
                    format="%d-%m-%Y %H:%M:%S",
                    errors="coerce"
                )

                executed_time = pd.to_datetime(
                    task_info.get("executed_time"),
                    format="%d-%m-%Y %H:%M:%S",
                    errors="coerce"
                )

                processing_time_hours = None

                if (
                    pd.notnull(received_time)
                    and pd.notnull(executed_time)
                ):
                    processing_time_hours = (
                        executed_time - received_time
                    ).total_seconds() / 3600

                records.append({

                    "task_history_key": task_history_key,

                    "application_id": application_id,

                    "appl_status": appl_status,

                    "task_name": task_info.get(
                        "task_name"
                    ),

                    "task_type": task_info.get(
                        "task_type"
                    ),

                    "designation": user_detail.get(
                        "designation"
                    ),

                    "location_name": user_detail.get(
                        "location_name"
                    ),

                    "user_name": user_detail.get(
                        "user_name"
                    ),

                    "task_action": task_info.get(
                        "task_action"
                    ),

                    "task_action_detail": task_info.get(
                        "task_action_detail"
                    ),

                    "received_time": received_time,

                    "executed_time": executed_time,

                    "current_process_id": task_info.get(
                        "current_process_id"
                    ),

                    "processing_time_hours":
                        processing_time_hours
                })

                task_history_key += 1

    except Exception as e:

        print(
            f"Error processing application "
            f"{application_id}: {e}"
        )

        continue

# -------------------------
# CREATE DATAFRAME
# -------------------------

task_history_df = pd.DataFrame(records)

print(
    "Task records:",
    len(task_history_df)
)

print(task_history_df.head())

# -------------------------
# LOAD TO POSTGRES
# -------------------------

task_history_df.to_sql(
    "fact_task_history",
    engine,
    schema="analytics",
    if_exists="replace",
    index=False
)

print(
    "fact_task_history loaded successfully"
)