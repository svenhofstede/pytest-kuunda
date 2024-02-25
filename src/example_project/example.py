from pyspark.sql import DataFrame
import pyspark.sql.functions as f


def add_one(df: DataFrame):
    return df.withColumn("value_add_one", f.col("value") + 1)
