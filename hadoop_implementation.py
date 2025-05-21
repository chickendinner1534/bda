import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["HADOOP_HOME"] = "/usr/local/hadoop"
os.environ["PATH"] = f"{os.environ['HADOOP_HOME']}/bin:{os.environ['PATH']}"

# Configure core-site.xml for local filesystem access
core_site = """
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>file:///</value>
  </property>
</configuration>
"""
with open("/usr/local/hadoop/etc/hadoop/core-site.xml", "w") as f:
    f.write(core_site)

# Create demo file and run Hadoop file management commands
!echo "This is a demo file for Hadoop" > demo.txt

print("\n[1] Creating directories in HDFS...")
!hadoop fs -mkdir /mydir
!hadoop fs -mkdir /mydir/subdir

print("\n[2] Listing root directory:")
!hadoop fs -ls /

print("\n[3] Adding file to HDFS...")
!hadoop fs -put demo.txt /mydir

print("\n[4] Listing contents of /mydir:")
!hadoop fs -ls /mydir

print("\n[5] Reading file from HDFS:")
!hadoop fs -cat /mydir/demo.txt

print("\n[6] Copying file from HDFS to local...")
!hadoop fs -get /mydir/demo.txt downloaded_demo.txt
!cat downloaded_demo.txt

print("\n[7] Deleting file from HDFS...")
!hadoop fs -rm /mydir/demo.txt

print("\n[8] Deleting directory from HDFS...")
!hadoop fs -rm -r /mydir
