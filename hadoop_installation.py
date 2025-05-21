!apt-get update
!apt-get install openjdk-8-jdk -y
!wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
!tar -xvzf hadoop-3.3.6.tar.gz
!mv hadoop-3.3.6 /usr/local/hadoop
import os

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["HADOOP_HOME"] = "/usr/local/hadoop"
os.environ["PATH"] = os.environ["HADOOP_HOME"] + "/bin:" + os.environ["HADOOP_HOME"] + "/sbin:" + os.environ["PATH"]
!/usr/local/hadoop/bin/hadoop version
