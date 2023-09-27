from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from demo_etl_pipeline.config.ConfigStore import *
from demo_etl_pipeline.udfs.UDFs import *
from prophecy.utils import *
from demo_etl_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_virgil_poc_dataset = virgil_poc_dataset(spark)
    df_Reformat_1 = Reformat_1(spark, df_virgil_poc_dataset)
    df_Filter_1 = Filter_1(spark, df_Reformat_1)
    df_OrderBy_1 = OrderBy_1(spark, df_Filter_1)
    virgil_poc_write(spark, df_OrderBy_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/demo_etl_pipeline")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/demo_etl_pipeline", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/demo_etl_pipeline")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
