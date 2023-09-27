from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_etl_pipeline.config.ConfigStore import *
from demo_etl_pipeline.udfs.UDFs import *

def virgil_poc_dataset(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(StructType([StructField("customer_id", StringType(), True), StructField("first_name", StringType(), True)]))\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Prophecy/45cd0a2f311d21e2b47c79c323ecf8a9/CustomersDatasetInput.csv")
