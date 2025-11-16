from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, upper, to_date
from config import config

spark = SparkSession.builder.appName("CarSalesBronzeToSilver").getOrCreate()

bronze_df = spark.read.format("delta").load(config.bronze_path)

silver_df = (
    bronze_df
    .withColumn("sale_date", to_date(col("sale_date"), "yyyy-MM-dd"))
    .withColumn("brand", upper(trim(col("brand"))))
    .withColumn("model", trim(col("model")))
    .withColumn("country", upper(trim(col("country"))))
    .dropDuplicates(["sale_id"])
)

(
    silver_df.write.mode("overwrite")
    .format("delta")
    .partitionBy("sale_date")
    .save(config.silver_path)
)

print(f"Wrote silver dataset to {config.silver_path}")
