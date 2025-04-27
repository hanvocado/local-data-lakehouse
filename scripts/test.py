from pyspark.sql import SparkSession
import os

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

spark = (
    SparkSession.builder
    .appName("lakehouse-test")
    .config("spark.hadoop.fs.s3a.access.key", AWS_ACCESS_KEY)
    .config("spark.hadoop.fs.s3a.secret.key", AWS_SECRET_KEY)
    .config("spark.executor.memory", "4g") 
    .config("spark.executor.cores", "2") 
    .config("spark.driver.memory", "4g")  
    .config("spark.driver.cores", "2")  
    .getOrCreate()
)

print("Spark is running")

spark.sql("CREATE DATABASE IF NOT EXISTS lakehouse.test_db")
spark.sql("SHOW TABLES IN lakehouse.test_db")

spark.sql("""
    CREATE TABLE IF NOT EXISTS lakehouse.test_db.names (
        name STRING
    )
    USING iceberg
""")

spark.sql("""
    INSERT INTO lakehouse.test_db.names VALUES 
    ('Alex Merced'), 
    ('Dipankar Mazumdar'), 
    ('Han Nguyen')
""")

spark.sql("SELECT * FROM lakehouse.test_db.names").show()

