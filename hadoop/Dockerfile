FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
      openjdk-17-jdk-headless python3 openssh-server openssh-client \
      curl ca-certificates procps \
    && rm -rf /var/lib/apt/lists/*

ENV HADOOP_VERSION=3.3.6
RUN curl -fsSL https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz \
      | tar -xz -C /opt \
    && ln -s /opt/hadoop-${HADOOP_VERSION} /opt/hadoop

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

WORKDIR /app
RUN mkdir -p /run/sshd /root/.ssh && ssh-keygen -t rsa -P "" -f /root/.ssh/id_rsa && cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys && chmod 600 /root/.ssh/authorized_keys
CMD ["bash", "-c", "service ssh start && sleep infinity"]
