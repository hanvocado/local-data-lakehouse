#!/bin/bash

if [ "${SPARK_MODE}" == "master" ]; then
    start-master.sh -p 7077
elif [ "${SPARK_MODE}" == "worker" ]; then
    start-worker.sh "${SPARK_MASTER_URL:-spark://spark-master:7077}"
else
    echo "Unknown SPARK_MODE: ${SPARK_MODE}"
    exit 1
fi
