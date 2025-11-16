from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum
from config import config

spark = SparkSession.builder.appName("CarSalesSilverToGold").getOrCreate()

silver_df = spark.read.format("delta").load(config.silver_path)

# Example: monthly revenue by brand and country
gold_df = (
    silver_df
    .withColumn("year_month", col("sale_date").substr(1, 7))
    .groupBy("year_month", "brand", "country")
    .agg(
        _sum("quantity").alias("total_units"),
        _sum("sale_amount").alias("total_revenue")
    )
)

(
    gold_df.write.mode("overwrite")
    .format("delta")
    .partitionBy("year_month")
    .save(config.gold_path)
)

print(f"Wrote gold aggregates to {config.gold_path}")
