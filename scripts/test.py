from pyspark.sql import SparkSession
import os

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID") ## AWS CREDENTIALS
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY") ## AWS CREDENTIALS

spark = (
    SparkSession.builder
    .appName("test")
    .config("spark.hadoop.fs.s3a.access.key", AWS_ACCESS_KEY)
    .config("spark.hadoop.fs.s3a.secret.key", AWS_SECRET_KEY)
    .getOrCreate()
)

print("Spark Running")

spark.sql("CREATE TABLE nessie.names (name STRING) USING iceberg;")

spark.sql("INSERT INTO nessie.names VALUES ('Alex Merced'), ('Dipankar Mazumdar'), ('Han Nguyen')")

spark.sql("SELECT * FROM nessie.names;").show()
