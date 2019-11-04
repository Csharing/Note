# Hbase，mysql，SHC Jar包
mkdir /opt/spark/spark-2.3.2-bin-hadoop2.7/jars/hbase &&\
/bin/cp $HBASE_HOME/lib/hbase*.jar /opt/spark/spark-2.3.2-bin-hadoop2.7/jars/hbase &&\
/bin/cp $HBASE_HOME/lib/guava-*.jar /opt/spark/spark-2.3.2-bin-hadoop2.7/jars/hbase &&\
/bin/cp $HBASE_HOME/lib/htrace-core*.jar /opt/spark/spark-2.3.2-bin-hadoop2.7/jars/hbase &&\
/bin/cp $HBASE_HOME/lib/protobuf-java*.jar /opt/spark/spark-2.3.2-bin-hadoop2.7/jars/hbase &&\
/bin/cp $HBASE_HOME/lib/metrics-core-*.jar /opt/spark/spark-2.3.2-bin-hadoop2.7/jars/hbase &&\
/bin/cp  /root/mysql-connector-java-8.0.16.jar /opt/spark/spark-2.3.2-bin-hadoop2.7/jars/
/bin/cp  /root/shc-core-spark-2.3.2-hbase-2.0.1.jar /opt/spark/spark-2.3.2-bin-hadoop2.7/jars/

# yarn模式下需要将依赖的jar包上传至集群
hadoop fs -mkdir -p  /spark-yarn/jars
hdfs dfs -put /opt/spark/spark-2.3.2-bin-hadoop2.7/jars/* /spark-yarn/jars/

# 配置slaves
echo 'worker4
worker5' > /opt/spark/spark-2.3.2-bin-hadoop2.7/conf/slaves


# 配置环境和conf
cp /opt/spark/spark-2.3.2-bin-hadoop2.7/conf/spark-env.sh.template /opt/spark/spark-2.3.2-bin-hadoop2.7/conf/spark-env.sh &&\
echo '
export SPARK_DIST_CLASSPATH=$(hadoop classpath):$(hbase classpath)
export  LD_LIBRARY_PATH=$HADOOP_HOME/lib/native
export SPARK_DAEMON_JAVA_OPTS="-Dspark.deploy.recoveryMode=ZOOKEEPER -Dspark.deploy.zookeeper.url=worker3:2181,worker4:2181,worker5:2181 -Dspark.deploy.zookeeper.dir=/spark"
' >> /opt/spark/spark-2.3.2-bin-hadoop2.7/conf/spark-env.sh

/bin/cp /opt/spark/spark-2.3.2-bin-hadoop2.7/conf/spark-defaults.conf.template /opt/spark/spark-2.3.2-bin-hadoop2.7/conf/spark-defaults.conf &&\
echo 'spark.yarn.jars=hdfs://NameNs/spark-yarn/jars/*.jar
spark.eventLog.enabled=false
' >> /opt/spark/spark-2.3.2-bin-hadoop2.7/conf/spark-defaults.conf


# hive 配置文件
echo '<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>javax.jdo.option.ConnectionURL</name>
        <value>jdbc:mysql://47.107.140.154:3306/hadoophive?allowMultiQueries=true&amp;useSSL=false&amp;verifyServerCertificate=false</value>
    </property>
    <property>
        <name>javax.jdo.option.ConnectionDriverName</name>
        <value>com.mysql.cj.jdbc.Driver</value>
    </property>
    <property>
        <name>javax.jdo.option.ConnectionUserName</name>
        <value>cshare</value>
    </property>
    <property>
        <name>javax.jdo.option.ConnectionPassword</name>
        <value>aBc123456.</value>
    </property>
    <property>
        <name>datanucleus.readOnlyDatastore</name>
        <value>false</value>
    </property>
    <property>
        <name>datanucleus.fixedDatastore</name>
        <value>false</value>
    </property>
    <property>
        <name>datanucleus.autoCreateSchema</name>
        <value>true</value>
    </property>
    <property>
        <name>datanucleus.autoCreateTables</name>
        <value>true</value>
    </property>
    <property>
        <name>datanucleus.autoCreateColumns</name>
        <value>true</value>
    </property>
    <property>
        <name>hive.support.concurrency</name>
        <value>true</value>
    </property>
    <property>
        <name>hive.zookeeper.quorum</name>
        <value>worker3:2181,worker4:2181,worker5:2181</value>
    </property>
    <property>
        <name>hbase.zookeeper.quorum</name>
        <value>worker3:2181,worker4:2181,worker5:2181</value>
    </property>
    <property>
        <name>hive.server2.thrift.port</name>
        <value>10000</value>
    </property>
    <property>
        <name>hive.server2.thrift.bind.host</name>
        <value>worker3</value>
    </property>
    <property>
        <name>hive.server2.transport.mode</name>
        <value>http</value>
    </property>
    <property>
        <name>hive.server2.authentication</name>
        <value>NOSASL</value>
    </property>
    <property>
        <name>hive.metastore.schema.verification</name>
        <value>FALSE</value>
    </property>
    <property>
        <name>hive.server2.enable.doAs</name>
        <value>FALSE</value>
    </property>
	<property>
        <name>hive.metastore.warehouse.dir</name>
        <value>/user/hive/warehouse</value>
    </property>
</configuration>
' >/opt/spark/spark-2.3.2-bin-hadoop2.7/conf/hive-site.xml