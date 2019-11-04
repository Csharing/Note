mv /opt/zookeeper/zookeeper-3.4.14/conf/zoo_sample.cfg /opt/zookeeper/zookeeper-3.4.14/conf/zoo.cfg &&\
sed -ri 's/\/tmp\/zookeeper/\/data\/zookeeper/g' /opt/zookeeper/zookeeper-3.4.14/conf/zoo.cfg &&\
cat >> /opt/zookeeper/zookeeper-3.4.14/conf/zoo.cfg <<EOF
server.1=worker3:2888:3888
server.2=worker4:2888:3888
server.3=worker5:2888:3888
EOF