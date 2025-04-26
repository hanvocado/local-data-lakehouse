FROM python:3.10-bullseye

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        sudo \
        curl \
        vim \
        ssh \
        openjdk-11-jdk && \
    apt-get clean && \
    # remove apt cached, docker already cached layers
    rm -rf /var/lib/apt/lists/* 

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

ENV HADOOP_VERSION=3.2
ENV SPARK_VERSION=3.2.1
ENV SPARK_HOME=/opt/spark
ENV WORK_HOME=/opt/work
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

RUN mkdir -p ${WORK_HOME} && mkdir -p ${SPARK_HOME}
WORKDIR ${SPARK_HOME}

RUN curl -fSL https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -o spark.tgz && \
    tar xvzf spark.tgz --directory /opt/spark --strip-components 1 && \
    rm -rf spark.tgz    

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./conf/spark-defaults.conf ${SPARK_HOME}/conf/

RUN chmod u+x /opt/spark/sbin/* \
    && chmod u+x /opt/spark/bin/*

RUN useradd -ms /bin/bash sparkuser && echo 'sparkuser:sparkuser' | chpasswd && \
    chown -R sparkuser:sparkuser ${SPARK_HOME} ${WORK_HOME}

USER sparkuser

COPY entrypoint.sh .

ENV SPARK_NO_DAEMONIZE=true

ENTRYPOINT [ "./entrypoint.sh" ]
