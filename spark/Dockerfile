FROM bitnami/spark:3.5

ENV SPARK_HOME=/opt/bitnami/spark

COPY ./conf/spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf

USER root

RUN echo "sparkuser:x:1001:1001::/home/sparkuser:/bin/bash" >> /etc/passwd

USER sparkuser
