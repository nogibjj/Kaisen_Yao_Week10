"""
library functions for FIFA data analysis
"""

import os
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType

LOG_FILE = "pyspark_output.md"


def log_output(operation, output, query=None):
    """adds to a markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query:
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is: \n\n")
        file.write(output)
        file.write("\n\n")


def start_spark(appName):
    """Start a Spark session"""
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark


def end_spark(spark):
    """End the Spark session"""
    spark.stop()
    return "stopped spark session"


def extract(
    url="""
    https://github.com/fivethirtyeight/data/blob/master/fifa/fifa_countries_audience.csv?raw=true
    """,
    file_path="data/fifa_countries_audience.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path


def load_data(spark, data="data/fifa_countries_audience.csv", name="fifa"):
    """load FIFA data with schema"""
    schema = StructType(
        [
            StructField("country", StringType(), True),
            StructField("confederation", StringType(), True),
            StructField("population_share", FloatType(), True),
            StructField("tv_audience_share", FloatType(), True),
            StructField("gdp_weighted_share", FloatType(), True),
        ]
    )

    df = spark.read.option("header", "true").schema(schema).csv(data)
    log_output("load data", df.limit(10).toPandas().to_markdown())
    return df


def query(spark, df, query, name="fifa"):
    """queries using spark sql"""
    df.createOrReplaceTempView(name)
    log_output("query data", spark.sql(query).toPandas().to_markdown(), query)
    return spark.sql(query).show()


def describe(df):
    """Get basic statistics of the numeric columns"""
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)
    return df.describe().show()


def example_transform(df):
    """Transform FIFA data to add region categories"""
    conditions = [
        (col("confederation") == "AFC") | (col("confederation") == "UEFA"),
        (col("confederation") == "CONCACAF") | (col("confederation") == "CONMEBOL"),
    ]
    categories = ["Eurasia", "Americas"]

    df = df.withColumn(
        "region_category",
        when(conditions[0], categories[0])
        .when(conditions[1], categories[1])
        .otherwise("Other"),
    )

    log_output("transform data", df.limit(10).toPandas().to_markdown())
    return df.show()
