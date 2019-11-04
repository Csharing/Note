# --------------------------------- 初始化----------------------------- #

[root@worker3]# mkdir -p /data/hadoop/dfs/name
[root@worker4]# mkdir -p /data/hadoop/dfs/name
[root@worker5]# mkdir -p /data/hadoop/dfs/name

[root@worker3]# mkdir /data/zookeeper && echo 1 > /data/zookeeper/myid
[root@worker4]# mkdir /data/zookeeper && echo 2 > /data/zookeeper/myid
[root@worker5]# mkdir /data/zookeeper && echo 3 > /data/zookeeper/myid

[root@worker3]# mkdir -p /data/hbase/tmp
[root@worker4]# mkdir -p /data/hbase/tmp
[root@worker5]# mkdir -p /data/hbase/tmp

[root@worker3]# schematool -dbType mysql -initSchema

# -------------------------------- 启动集群---------------------------- #
# ZooKeeper
[root@worker3]# zkServer.sh start
[root@worker4]# zkServer.sh start
[root@worker5]# zkServer.sh start


# Hdfs-HA  start-all.sh
# This script is Deprecated. Instead use start-dfs.sh and start-yarn.sh
[root@worker3]# hdfs zkfc -formatZK

[root@worker3]# hadoop-daemon.sh start journalnode
[root@worker4]# hadoop-daemon.sh start journalnode
[root@worker5]# hadoop-daemon.sh start journalnode

[root@worker3]# hdfs namenode -format NameNs
[root@worker3]# hadoop-daemon.sh start namenode
[root@worker3]# hadoop-daemon.sh start zkfc

[root@worker4]# hdfs namenode -bootstrapStandby
[root@worker4]# hadoop-daemon.sh start namenode
[root@worker4]# hadoop-daemon.sh start zkfc

[root@worker3]# hadoop-daemon.sh start datanode
[root@worker4]# hadoop-daemon.sh start datanode
[root@worker5]# hadoop-daemon.sh start datanode

	
# Yarn
[root@worker3]# yarn-daemon.sh start resourcemanager
[root@worker4]# yarn-daemon.sh start resourcemanager
[root@worker3]# yarn-daemon.sh start nodemanager
[root@worker4]# yarn-daemon.sh start nodemanager
[root@worker5]# yarn-daemon.sh start nodemanager


# Hbase-HA start-hbase.sh
[root@worker3]# hbase-daemon.sh start master
[root@worker3]# hbase-daemon.sh start master
[root@worker3]# hbase-daemon.sh start regionserver
[root@worker3]# hbase-daemon.sh start regionserver
[root@worker3]# hbase-daemon.sh start regionserver


# Hive
hive --service metastore >/dev/null 2>/dev/null &
hive --service hiveserver2 >/dev/null 2>/dev/null &


# Spark-HA
[root@worker3]# /opt/spark/spark-2.3.2-bin-hadoop2.7/sbin/start-master.sh
[root@worker4]# /opt/spark/spark-2.3.2-bin-hadoop2.7/sbin/start-master.sh
[root@worker4]# /opt/spark/spark-2.3.2-bin-hadoop2.7/sbin/start-slave.sh spark://worker3:7077
[root@worker5]# /opt/spark/spark-2.3.2-bin-hadoop2.7/sbin/start-slave.sh spark://worker3:7077


# Hue
[root@worker3]# mr-jobhistory-daemon.sh start historyserver
[root@worker3]# httpfs.sh start
[root@worker3]# hbase-daemon.sh start thrift