from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
from config import config

spark = SparkSession.builder.appName("CarSalesIngestRawToBronze").getOrCreate()

# In Databricks, this might be a mount or a linked service path
raw_source_path = "/mnt/raw/car_sales/*.csv"

df_raw = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(raw_source_path)
    .withColumn("ingested_at_utc", current_timestamp())
)

(
    df_raw.write.mode("overwrite")
    .format("delta")
    .save(config.bronze_path)
)

print(f"Wrote {df_raw.count()} records to {config.bronze_path}")
