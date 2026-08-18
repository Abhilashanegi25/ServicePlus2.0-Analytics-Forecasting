from sqlalchemy import create_engine
import pandas as pd
from db_config import DATABASE_URL

engine = create_engine(DATABASE_URL)

query = """
SELECT
    application_id,
    execution_data
FROM data_stats
ORDER BY application_id
LIMIT 10000
"""

df = pd.read_sql(query, engine)

print("Rows loaded:", len(df))

task_records = []

for _, row in df.iterrows():

    application_id = row["application_id"]
    execution_data = row["execution_data"]

    if not execution_data:
        continue

    for group in execution_data:

        for task in group:

            task_info = task.get("task_info", {})

            received_time = task_info.get("received_time")
            executed_time = task_info.get("executed_time")

            duration_days = None

            if received_time and executed_time:

                received_ts = pd.to_datetime(
                    received_time,
                    format="%d-%m-%Y %H:%M:%S",
                    errors="coerce"
                )

                executed_ts = pd.to_datetime(
                    executed_time,
                    format="%d-%m-%Y %H:%M:%S",
                    errors="coerce"
                )

                if pd.notnull(received_ts) and pd.notnull(executed_ts):

                    duration_days = (
                        executed_ts - received_ts
                    ).total_seconds() / 86400

            task_records.append({
                "application_id": application_id,
                "task_id": task_info.get("task_id"),
                "task_name": task_info.get("task_name"),
                "task_type": task_info.get("task_type"),

                "received_time": received_time,
                "executed_time": executed_time,

                "action_taken": task_info.get("action_taken"),
                "task_action_detail": task_info.get("task_action_detail"),

                "duration_days": duration_days
            })

task_history = pd.DataFrame(task_records)

print("Before dedup:", len(task_history))

task_history = task_history.drop_duplicates(
    subset=["application_id", "task_id"]
)

print("After dedup:", len(task_history))

print("Task records:", len(task_history))

task_history.to_sql(
    "fact_task_history",
    engine,
    schema="analytics",
    if_exists="replace",
    index=False
)

print("fact_task_history loaded successfully")
