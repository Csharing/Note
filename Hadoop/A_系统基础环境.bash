#-------------------------- 系统环境 -------------------------- #

# 网卡
cat >> /etc/sysconfig/network-scripts/ifcfg-eth0 <<EOF
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=eth0
UUID=da4cffb1-2bbd-48b9-98c8-f23ce8231799
DEVICE=eth0
ONBOOT=yes
IPADDR=172.26.44.93
NETMASK=255.255.255.240
GATEWAY=172.26.44.81
EOF

# DNS解析
echo '
nameserver 8.8.8.8
nameserver 8.8.4.4
' > /etc/resolv.conf

# 主机名
hostnamectl --static set-hostname worker3

# 其他主机
cat > /etc/hosts <<EOF
172.26.44.93 worker3
172.26.44.94 worker4
172.26.44.89 worker5
EOF

# ssh服务
sed -ri 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && \
systemctl start sshd && systemctl enable sshd

# 生成秘钥
ssh-keygen -t rsa -C "1193543051@qq.com" -P "" -f ~/.ssh/id_rsa

# 关闭防火墙
systemctl stop firewalld && systemctl disable firewalld

# 同步时间
yum -y install ntp ntpdate
ntpdate cn.pool.ntp.org


#-------------------------- 解压和同步文件 ---------------- ---- #
mkdir /opt/java && tar -zxf /root/jdk-8u211-linux-x64.tar.gz -C /opt/java
mkdir /opt/zookeeper && tar -zxf /root/zookeeper-3.4.14.tar.gz -C /opt/zookeeper
mkdir /opt/hadoop && tar -zxf /root/hadoop-2.7.4.tar.gz -C /opt/hadoop
mkdir /opt/hbase && tar -zxf /root/hbase-2.0.1-bin.tar.gz -C /opt/hbase
mkdir /opt/hive && tar -zxf /root/apache-hive-3.1.1-bin.tar.gz -C /opt/hive
mkdir /opt/spark && tar -zxf /root/spark-2.3.2-bin-hadoop2.7.tgz -C /opt/spark

mkdir /opt/ant && tar -zxf /root/apache-ant-1.10.6-bin.tar.gz -C /opt/ant
mkdir /opt/maven && tar -zxf /root/apache-maven-3.6.1-bin.tar.gz -C /opt/maven
mkdir /opt/hue && tar -zxf /root/hue-release-4.3.0.tar.gz -C /opt/hue

ssh-copy-id root@worker3
ssh-copy-id root@worker4
ssh-copy-id root@worker5
 
rm -rf /opt/zookeeper/zookeeper-3.4.14/zookeeper-docs
scp -r /opt/zookeeper/* root@worker4:/opt/zookeeper/
scp -r /opt/zookeeper/* root@worker5:/opt/zookeeper/

rm -rf /opt/hadoop/hadoop-2.7.4/share/doc
scp -r /opt/hadoop/* root@worker4:/opt/hadoop/
scp -r /opt/hadoop/* root@worker5:/opt/hadoop/

rm -rf /opt/hbase/hbase-2.0.1/docs
rm -f /opt/hbase/hbase-2.0.1/lib/slf4j-log4j12-1.7.25.jar
scp -r /opt/hbase/* root@worker4:/opt/hbase/
scp -r /opt/hbase/* root@worker5:/opt/hbase/

rm -rf /opt/spark/spark-2.3.2-bin-hadoop2.7/jars/slf4j-log4j12-1.7.16.jar
scp -r /opt/spark/* root@worker4:/opt/spark/
scp -r /opt/spark/* root@worker5:/opt/spark/

#-------------------------- Python3 --------------------------- #
yum install -y libffi-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make  > /dev/null && \
tar -zxf /root/Python-3.7.0.tgz -C /root && \
cd /root/Python-3.7.0 && \
/root/Python-3.7.0/configure prefix=/usr/local/python3 && \
make  > /dev/null && \
make install > /dev/null && \
make clean && \
ln -s /usr/local/python3/bin/python3 /usr/bin/python3 && \
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3



#----------------------- 配置系统环境变量 --------------------- #
echo '
#ant
export ANT_HOME=/opt/ant/apache-ant-1.10.6
export PATH=$PATH:$ANT_HOME/bin


#hive
export HIVE_HOME=/opt/hive/apache-hive-3.1.1-bin
export PATH=$PATH:$HIVE_HOME/bin


#maven
export MAVEN_HOME=/opt/maven/apache-maven-3.6.1
export PATH=$PATH:$MAVEN_HOME/bin


#hadoop
export HADOOP_HOME=/opt/hadoop/hadoop-2.7.4
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib:$HADOOP_COMMON_LIB_NATIVE_DIR"
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop


#hbase
export HBASE_HOME=/opt/hbase/hbase-2.0.1
export PATH=$PATH:$HBASE_HOME/bin


#java
export JAVA_HOME=/opt/java/jdk1.8.0_211
export JRE_HOME=/opt/java/jdk1.8.0_211/jre
export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib


#zookeeper
export ZOOKEEPER_HOME=/opt/zookeeper/zookeeper-3.4.14
export PATH=$PATH:$ZOOKEEPER_HOME/bin


#spark
export SPARK_HOME=/opt/spark/spark-2.3.2-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/bin
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH
export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=python3
' >> /etc/profile && source /etc/profile