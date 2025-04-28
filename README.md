# Local Data Lakehouse Project

## Overview
This project is a robust implementation of a local data lakehouse architecture, designed to efficiently manage and query large datasets. Built with Docker Compose, the project integrates cutting-edge components such as compute engines, storage solutions, table formats, and SQL query engines to deliver a high-performing and scalable data management solution.

## Architecture

![LakeHouse architecture](https://raw.githubusercontent.com/hanvocado/data/main/diagram-lakehouse1.jpg)

The data lakehouse architecture incorporates the following components:
- **Compute Engine**: A Apache Spark cluster for distributed data processing. To scale vertically, increase spark-worker containers' resources. To scale horizontally, run:
    ```bash
    docker-compose up --scale spark-worker=<n>
    ```
    ![Spark cluster](https://raw.githubusercontent.com/hanvocado/data/main/local-lakehouse-spark-upload-test.png)

- **Table Format**: Apache Iceberg for reliable and efficient data management with ACID properties.
- **Storage**: MinIO (S3-compatible) object storage system.
- **Catalog**: Hive as a metastore service and PostgreSQL stores the actual metadata.
- **SQL Query Engine**: Dremio to enable fast and interactive SQL queries on the data.

    ![SQL sales query](https://raw.githubusercontent.com/hanvocado/data/main/local-lakehouse-dremio.png)

## Future Work
I will update this project with an ETL pipeline.
