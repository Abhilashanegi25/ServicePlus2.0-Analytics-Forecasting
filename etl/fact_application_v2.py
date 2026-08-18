from sqlalchemy import create_engine
import pandas as pd
from db_config import DATABASE_URL

engine = create_engine(DATABASE_URL)

query = """
SELECT
    application_id,
    initiated_data,
    execution_data
FROM data_stats
ORDER BY application_id
LIMIT 10000
"""

df = pd.read_sql(query, engine)

print("Before dedup:", len(df))

df = df.drop_duplicates(
    subset=["application_id"]
)

print("After dedup:", len(df))

prefixes = [
    "Aadhaar Verification by State Portal - ",
    "Aadhaar Verification by State portal - ",
    "Aadhaar Verification by State Portal-",
    "Aadhaar Verification by State portal-",
    "Aadhaar Verification Portal by State - ",
    "Aadhaar Verification Portal by State- ",
    "Aadhaar Verification Portal by State-"
]

fact_records = []

for _, row in df.iterrows():

    record = row["initiated_data"]
    appl_info = record["appl_info"]

    service_name = appl_info.get("service_name", "")

    state = service_name

    for p in prefixes:
        state = state.replace(p, "")

    state = state.strip()

    completion_time = None

    execution_data = row["execution_data"]

    if execution_data:

        all_times = []

        for group in execution_data:

            for task in group:

                task_info = task.get("task_info", {})

                executed_time = task_info.get("executed_time")

                if executed_time:

                    ts = pd.to_datetime(
                        executed_time,
                        format="%d-%m-%Y %H:%M:%S",
                        errors="coerce"
                    )

                    if pd.notnull(ts):
                        all_times.append(ts)

        if all_times:
            completion_time = max(all_times)

    fact_records.append({
        "application_id": appl_info.get("appl_id"),
        "service_key": appl_info.get("service_id"),
        "appl_ref_no": appl_info.get("appl_ref_no"),
        "submission_date": appl_info.get("submission_date"),
        "due_date": appl_info.get("due_date"),
        "state": state,
        "completion_time": completion_time
    })

fact_application = pd.DataFrame(fact_records)

print("Fact records:", len(fact_application))

fact_application.to_sql(
    "fact_application",
    engine,
    schema="analytics",
    if_exists="replace",
    index=False
)

print("fact_application loaded successfully")
