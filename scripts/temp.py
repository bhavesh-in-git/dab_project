from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.serverless(True).getOrCreate()
(spark.sql("Select 1")).show()
spark.stop()