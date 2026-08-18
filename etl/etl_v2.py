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

# =====================================================
# DIM SERVICE
# =====================================================

service_records = []

for _, row in df.iterrows():

    record = row["initiated_data"]
    appl_info = record["appl_info"]

    service_name = appl_info.get("service_name")

    service_records.append({
        "service_key": appl_info.get("service_id"),
        "service_id": appl_info.get("service_id"),
        "base_service_id": appl_info.get("base_service_id"),
        "service_name": service_name,
        "department_id": appl_info.get("department_id"),
        "department_name": appl_info.get("department_name")
    })

dim_service = pd.DataFrame(service_records)

dim_service = dim_service.drop_duplicates(
    subset=["service_id"]
)

print("Unique services:", len(dim_service))

dim_service.to_sql(
    "dim_service",
    engine,
    schema="analytics",
    if_exists="replace",
    index=False
)

print("dim_service loaded successfully")
