# 配置hbase-env.sh
echo '
export HBASE_MANAGES_ZK=false
export JAVA_HOME=/opt/java/jdk1.8.0_211
' >> /opt/hbase/hbase-2.0.1/conf/hbase-env.sh

#配置regionservers，一起启动
cat > /opt/hbase/hbase-2.0.1/conf/regionservers <<EOF
worker3
worker4
worker5
EOF

#配置备用master
echo 'worker4' > /opt/hbase/hbase-2.0.1/conf/backup-masters

# 配置hbase-site.xml
sed -i '/^<configuration>/,/<\/configuration>$/d' /opt/hbase/hbase-2.0.1/conf/hbase-site.xml &&\
cat >> /opt/hbase/hbase-2.0.1/conf/hbase-site.xml <<EOF
<configuration>
    <property>
        <name>hbase.rootdir</name>
        <value>hdfs://NameNs/hbase</value>
    </property>
    <property>
        <name>hbase.cluster.distributed</name>
        <value>true</value>
    </property>
    <property>
        <name>hbase.master</name>
        <value>60000</value>
    </property>
    <property>
        <name>hbase.tmp.dir</name>
        <value>/data/hbase/tmp</value>
    </property>
    <property>
        <name>hbase.zookeeper.quorum</name>
        <value>worker3,worker4,worker5</value>
    </property>
    <property>
        <name>hbase.zookeeper.property.dataDir</name>
        <value>/data/zookeeper</value>
    </property>
    <property>
        <name>hbase.zookeeper.property.clientPort</name>
        <value>2181</value>
    </property>
    <property>
        <name>zookeeper.session.timeout</name>
        <value>120000</value>
    </property>
    <property>
        <name>hbase.regionserver.restart.on.zk.expire</name>
        <value>true</value>
    </property>
</configuration>
EOF