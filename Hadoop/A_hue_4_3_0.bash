# 基础环境
yum install -y asciidoc cyrus-sasl-devel cyrus-sasl-gssapi cyrus-sasl-plain gcc gcc-c++ krb5-devel libffi-devel libxml2-devel libxslt-devel make mysql mysql-devel openldap-devel python-devel sqlite-devel gmp-devel openssl-devel

# Python2.7下安装pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py 

# 安装nodejs
wget https://nodejs.org/dist/v9.8.0/node-v9.8.0-linux-x64.tar.xz
tar --strip-components 1 -xf node-v* -C /usr/local

# 解压hue，编译
cd /opt/hue/hue-release-4.3.0
make apps

# 启动报"Couldn't get user id for user hue"，不能用root用户启动，那就新建用户，然后改权限，操
useradd hue && echo "123456" | passwd --stdin hue
chown -R hue /opt/hue

# 启动
/opt/hue/hue-release-4.3.0/build/env/bin/supervisor  >> /home/hue/log/hue.log 2>&1 &
#同步库
/opt/hue/hue-release-4.3.0/build/env/bin/hue syncdb
#初始化&迁移库
/opt/hue/hue-release-4.3.0/build/env/bin/hue migrate


#----------------------------------------Hadoop----------------------------------------#

# 增加下面配置httpfs-site.xml
    <property>
        <name>httpfs.proxyuser.hue.hosts</name>
        <value>*</value>
    </property>
    <property>
        <name>httpfs.proxyuser.hue.groups</name>
        <value>*</value>
    </property>

# 配置pseudo-distributed，太复杂，看文档吧
# 将需要用的组件配置文件统一放在hue的家目录下，妈的，不能用root启动，现在又要获取其他组建的配置文件，权限真鸡儿坑
mkdir /home/hue/hadoopconf/ && cp /opt/hadoop/hadoop-2.9.0/etc/hadoop/* /home/hue/hadoopconf/ && chown -R hue /home/hue/hadoopconf/
mkdir /home/hue/hiveconf/ && cp /opt/hive/apache-hive-3.1.1-bin/conf/* /home/hue/hiveconf/ && chown -R hue /home/hue/hiveconf/


#----------------------------------------hbase----------------------------------------#
pseudo-distributed.ini
	[hbase]
	  hbase_clusters=(Cluster|manager:9090)
	  hbase_conf_dir=/home/hue/hbaseconf/
	  truncate_limit = 500
	  thrift_transport=buffered
  
# 启动hbase的第三方接口，服务暴露端口 #lsof -i:9090
hbase-daemon.sh start thrift
# 拷贝环境
mkdir /home/hue/hbaseconf/ && cp /opt/hbase/hbase-1.4.10/conf/* /home/hue/hbaseconf/ && chown -R hue /home/hue/hbaseconf/




#----------------------------------------Spark----------------------------------------#

#spark需要安装spark-jobserver，而安装spark-jobserver又需要安装scala的构建工具SBT
#使用scala2.11，不要用scala2.10，package的时候没有对应上，真坑，还要用find主动找
# 安装SBT
curl https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-sbt-rpm.repo
yum -y install sbt

#初始化SBT，会下一些东西，贼tm慢
sbt version 

# 安装spark-jobserver
wget https://github.com/spark-jobserver/spark-jobserver/archive/v0.9.0.tar.gz
tar -zxf v0.9.0.tar.gz
cd spark-jobserver/

# 配置阿里仓库，自带的很慢
echo '[repositories]
local
aliyun-nexus: http://maven.aliyun.com/nexus/content/groups/public/  
typesafe: http://repo.typesafe.com/typesafe/ivy-releases/, [organization]/[module]/(scala_[scalaVersion]/)(sbt_[sbtVersion]/)[revision]/[type]s/[artifact](-[classifier]).[ext], bootOnly
sonatype-oss-releases
maven-central
sonatype-oss-snapshots' > ~/.sbt/repositories

echo '<mirror>
  <id>alimaven</id>
  <name>aliyun maven</name>
  <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
  <mirrorOf>central</mirrorOf>
</mirror>' > ~/.m2/settings.xml

# 清sbt缓存
rm -rf ~/.sbt
rm -rf ~/.ivy2
rm -rf ~/.ivy

# copy配置文件
# shiro.ini认证Kerberos的，现在默认没有
cp /opt/spark/spark-jobserver/config/local.conf.template /opt/spark/spark-jobserver/config/local.conf &&\
cp /opt/spark/spark-jobserver/config/local.sh.template /opt/spark/spark-jobserver/config/local.sh

# 打包，部署
bin/server_package.sh local
bin/server_deploy.sh local

# 找job-server的jar包，scala2.10的坑
find /opt/spark/spark-jobserver -name "*job-server.jar"





