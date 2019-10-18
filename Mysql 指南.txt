SQL语句--mysql

一：设计数据库

	1.数据库(DATABASE)
	
		创建：mysql> CREATE DATABASE d1;
		删除：mysql> DROP DATABASE d1;
		查看：mysql> SHOW DATABASES;
			  mysql> SELECT DATABASE();
			  mysql> STATUS;
			  --所有的数据库列表，当前所用数据库，当前数据库的详细信息
		切换：mysql> USE d1；
	
	2.数据表(TABLE)
	
		创建：
		
			mysql> create table t1(
					ID int not null AUTO_INCREMENT,
					number1 int(10) UNSIGNED NOT NULL,
					number2 int NOT NULL,
					name1 varchar(255),
					name2 varchar(255)  comment '注释',
					name3 varchar(255) default 'Cshare',
					name4 Enum('a','b'),
					primary key (ID),
					check(number1>1),
					unique(name1)
					);
				
			mysql> CREATE TABLE t2 SELECT * FROM t3;
			--可用于备份
				
			特殊字段：
			
				AUTO INCREMENT--在新记录插入表中时生成一个唯一的数字，默认开始值为1，每次递增1
					mysql> ALTER TABLE t1 AUTO_INCREMENT=100
					--修改t1表的AUTO_INCREMENT的开始值为100
				
				UNSIGNED--非负数,范围从0开始
				
				ENUM--ENUM('a','b')
					枚举，无需定义数据类型，且只能为文本型
				
				注：最后一行不能加,
				
								 
		删除：
		
			mysql> DROP TABLE t1;
			mysql> DROP TABLE IF EXISTS t1;
			--删除t1表,需要用sql文件创建t1表时，可利用IF EXISTS来删除t1表而不会报错
			
		查看：
		
			mysql> SHOW TABLES;
			--查看当前数据库下的所有表
			mysql> SHOW COLUMNS FROM t1;
			mysql> DESC t1;
			--查看t1表的表结构
			mysql> SHOW CREATE TABLE t1;
			--查看t1表的创建信息，可找到自动生成的索引名称
		
		改动：
		
			mysql> ALTER TABLE t1 RENAME TO t2;
			--t1表重命名为t2表
			mysql> ALTER TABLE t1 ADD column1 ENUM('old','young') NOT NULL
			--t1表中添加column1列
			mysql> ALTER TABLE t1 DROP column1，DROP column2；
			--t1表中删除column1列
			mysql> ALTER TABLE t1 MODIFY COLUMN column1 INT;
			--修改column1的数据类型为int，可自定义多样化的datatype
			
	3.临时表(TEMPORARY)
	--在你断开连接时自动删除，用法同table
	
		mysql> CREATE TEMPORARY TABLE t1 SELECT * FROM t2;
		--创建时直接导入数据
		mysql> CREATE TEMPORARY TABLE t1(name VARCHAR(10) NOT NULL,value INTEGER NOT NULL) TYPE = HEAP ；  
		--HEAP表示在内存中直接创建，创建形式形如创建table
	
			
二：管理约束

	约束(CONSTRAINTS):
		
	  
		1.UNIQUE --约束唯一标识数据库表中的每条记录
	  
			CONSTRAINT cons1 UNIQUE (number1,number2),
			--创建表时命名UNIQUE约束
			mysql> ALTER TABLE t1 ADD UNIQUE (column1);
			--当表已被创建时，在columns1列创建UNIQUE约束
			mysql> ALTER TABLE t1 ADD CONSTRAINT cons2 UNIQUE (column1,column2);
			--当表存在时，定义多个列的 UNIQUE 约束
			mysql> ALTER TABLE t1 DROP INDEX cons2;
			--撤销UNIQUE约束
		
		2.PRIMARY KEY--约束唯一标识数据库表中的每条记录，UNIQUE和NOT NULL集合，每个表都应有且只有一个主键
	  
			CONSTRAINT cons1 PRIMARY KEY (number1,number2),
			--创建表时命名PRIMARY KEY约束
			mysql> ALTER TABLE t1 ADD PRIMARY KEY (column1);
			--当表已被创建时，在columns1列创建PRIMARY KEY约束,必须把主键列声明为不包含 NULL 值（在表首次创建时）
			mysql> ALTER TABLE t1 ADD CONSTRAINT cons2 PRIMARY KEY (column1,column2);
			--当表存在时，定义多个列的 PRIMARY KEY 约束
			mysql> ALTER TABLE t1 DROP PRIMARY KEY;
			--撤销PRIMARY KEY约束
		
		3.FOREIGN KEY --一个表中的 FOREIGN KEY 指向另一个表中的 PRIMARY KEY
	  
			CONSTRAINT cons1 FOREIGN KEY (number1) REFERENCES t2(number1),
			--创建表时命名FOREIGN KEY约束
			mysql> ALTER TABLE t1 ADD FOREIGN KEY (column1) REFERENCES t2(column1) ON DELETE CASCADE ON UPDATE CASCADE
			--当已被创建时，在column1列创建FOREIGN KEY约束,CASCADE表示同步删除和更新，详见参考【7】
			mysql> ALTER TABLE t1 ADD CONSTRAINT cons2 FOREIGN KEY (column1) REFERENCES t2(column1);
			--当表存在时，命名FOREIGN KEY约束
			mysql> ALTER TABLE t1 DROP FOREIGN KEY cons2;
			--撤销FOREIGN KEY约束
		 
		4.CHECK --约束用于限制列中的值的范围
	  
			CONSTRAINT cons1 CHECK (number1>0 AND name1='Cshare'),
			--创建表时命名CHECK约束
			mysql> ALTER TABLE t1 ADD CHECK (column1>0);
			--当已被创建时，在column1列创建CHECK约束
			mysql> ALTER TABLE t1 ADD CONSTRAINT cons2 CHECK (column1>0 AND column2='Cshare');
			--当表存在时，命名CHECK约束
			mysql> ALTER TABLE Persons DROP CHECK cons2;
			--撤销CHECK约束
		 
		5.DEFAULT --约束用于向列中插入默认值
		
			OrderDate DATE DEFAULT GETDATE(),
			--DEFAULT可以插入函数
			mysql> ALTER TABLE t1 ALTER column1 SET DEFAULT 'Cshare';
			--当已被创建时，在column1列创建DEFAULT约束
			mysql> ALTER TABLE t1 ALTER column1 DROP DEFAULT;
			--撤销DEFAULT约束
			
	索引(INDEX):
	
	--索引有四种：普通，唯一，主键，组合
		mysql> INDEX(num1)
		--创建表的时候加索引，也可以用KEY key1(num1)创建名为key1的索引
		mysql> SHOW INDEX FROM t1
		--查看索引
		mysql> CREATE INDEX index1 ON t1(column1,column2 DESC);
		--ASC降序，DESC升序，对涉及到查询的列创建
		mysql> ALTER TABLE t1 DROP INDEX index1;
		--删除索引
		
			
三：管理单表
	
	1.SELECT(子查询)
	
		*简单选取
		
			mysql> SELECT column1,column2 FROM t1;
			mysql> SELECT * FROM t1;
			mysql> SELECT DISTINCT column1 FROM t1;--去重
		
		*复杂选取
		
			--WHERE子句{=,<>,>,<,>=,<=,BETWEEN,LIKE，IN}
			
				mysql> SELECT * FROM t1 WHERE column1='Cshare';
				mysql> SELECT * FROM t1 WHERE column1>100;			
				mysql> SELECT * FROM t1 WHERE column1 BETWEEN value1 AND value2
				mysql> SELECT * FROM t1 WHERE column1 BETWEEN 'a' AND 'h';
				--BETWEEN可以是数字，文本，日期；包含value1，value2；NOT BETWEEN 相补
				--文本型时慎用
				mysql> SELECT * FROM t1 WHERE column1 LIKE 'c%'
				mysql> SELECT * FROM t1 WHERE column1 NOT LIKE '%c%'
				--'%'表示一个或多个,'_'表示一个，[charlist],[^charlist]表示字符列中的一个,也用于show语句
				mysql> SELECT * FROM t1 WHERE column1 IN (value1,value2,...)
				mysql> SELECT * FROM t1 WHERE column1 IN (SELECT column2 FROM t2)
				--IN,可以嵌套子查询
				
			--AND和OR运算符
			
				mysql> SELECT * FROM t1 WHERE column1='Cshare' AND column2>100;
				mysql> SELECT * FROM t1 WHERE column1='Cshare' OR column2>100;
				
			--ORDER BY语句(默认ASC表示升序，DESC表示降序） 
			
				mysql> SELECT * FROM t1 ORDER BY column1;
				mysql> SELECT * FROM t1 ORDER BY column1,column2;
				--column1升序下column2升序
				mysql> SELECT * FROM t1 ORDER BY column1 DESC;
				mysql> SELECT * FROM t1 ORDER BY column1 DESC,column2 ASC;
				--column1降序下column2升序
				
			--LIMIT语句
				mysql> SELECT * FROM t1 LIMIT 3;
				--选取前三条
				mysql> SELECT * FROM t1 LIMIT 2,3;
				--从第3条开始选取3条数据,第一个参数默认从0开始				
	
	2.INSERT
	
		mysql> INSERT INTO t1 VALUES(value1,value2,value3);
		--t1有多少列，values就要有多少值，into可以省略，但是INSERT INTO 是标准写法
		mysql> INSERT INTO t1(column1,column2) VALUES(value1,value2);
		mysql> INSERT t1 SET column1=value1,column2=value2;
		--column和value需要一一对应
		mysql> INSERT INTO t1(column1,column2) SELECT column3,column4 FROM t2
		--column1,column2与column3,column4的格式要对齐
		
	3.UPDATE
	
		mysql> UPDATE t1 SET column1=value1,column2=value2 WHERE column3='Cshare'
		--column1=value为赋值语句column1=column1+1也可，where提供一种多样化的筛选
	
	4.DELETE
		
		mysql> DELETE FROM t1 WHERE column1='Cshare';
		--删除某行
		mysql> DELETE FROM t1;
		mysql> DELETE * FROM t1;
		mysql> TRUNCATE TABLE t1;
		--清空表格
		
		
四：管理多表

	--别名 Aliases
	
		mysql> SELECT column1 FROM table1 AS t1
		mysql> SELECT column1 AS co1 FROM t1
		mysql> SELECT t1.column1,t2.column1 FROM table1 AS t1,table2 AS t2 
		--以column1，column2为列构成的表，若不足则最后一条数据向下填充
		
		
	JOIN:--用于根据两个或多个表中的列之间的关系，从这些表中查询数据
	
		mysql> SELECT t1.column1,t2.column1 WHERE t1.column2=t2.column2;
		--相同于INNER JOIN，当t1.column2与t2.column2分别含有n,m个相同重复值时，则会生成n*m条数据
		
		INNER JOIN--A∩B  在表中存在至少一个匹配时，INNER JOIN 关键字返回行
		mysql> SELECT t1.column1,t2.column1 FROM t1 INNER JOIN t2 ON t1.column2=t2.column2
		
		LEFT JOIN--A∩B∪A  关键字会从左表t1那里返回所有的行，即使在右表t2中没有匹配的行。
		mysql> SELECT t1.column1,t2.column1 FROM t1 LEFT JOIN t2 ON t1.column2=t2.column2
		
		RIGHT JOIN--A∩B∪B  关键字会从右表t1那里返回所有的行，即使在左表t2中没有匹配的行。
		mysql> SELECT t1.column1,t2.column1 FROM t1 RIGHT JOIN t2 ON t1.column2=t2.column2
		
		FULL JOIN--A∪B  只要其中某个表存在匹配，FULL JOIN 关键字就会返回行。
		mysql> SELECT t1.column1,t2.column1 FROM t1 FULL JOIN t2 ON t1.column2=t2.column2
		
		CROSS JOIN--笛卡尔连接，形成n*m列数据，不需要on后面子句
		
	
	UNION:--UNION操作符用于合并两个或多个具有相似结构的SELECT语句
	
		mysql> SELECT * FROM t1 UNION SELECT * FROM t2;
		--UNION操作符选取不同的值，如果允许重复的值，请使用 UNION ALL
		
		
五：创建视图

	VIEW:--视图的使用就像它是一张表
	
		创建
			mysql> CREATE VIEW view1 AS SELECT *FROM t1;
			
		查询
			mysql> SELECT * FROM view1;
			
		删除
			mysql> DROP VIEW view1;
			
			
六：SQL函数

	常用函数

		DATE函数
			mysql> SELECT now();
			--返回当前时间
			mysql> SELECT DATE(now());
			--提取日期
			mysql> SELECT DATE_FORMAT(NOW(),'%m/%d/%y');
			--指定日期格式，%Y2017|%y17
			
		NULL判断
			mysql> ……WHERE column1 IS NULL
			--判断是否为空，与IS NOT NULL 相补
			
		IFNULL()
			mysql> SELECT IFNULL(a,b);
			--如果a不为NULL则返回a，否则返回b
			
		IF()
			mysql> SELECT IF(a,b,c);
			--a=true返回b， a=false返回c
			
		GROUP BY
			mysql> SELECT SUM(id),name FROM t1 GROUP BY name;
			--以name分组处理数据，若不对id进行处理，则取第一个值
			
		HAVING 
			mysql> SELECT name FROM t1 GROUP BY name HAVING COUNT(name)<2;
			--在SQL中增加HAVING子句原因是WHERE关键字无法与合计函数一起使用。
			
		CONCAT()
			mysql> SELECT CONCAT(column1，column2) AS column3 FROM t1;
		--字符连接
		
		CONCAT_WS()
			mysql> SELECT CONCAT_WS('_',column1，column2) AS column3 FROM t1;
		--以指定符连接
		
		LENGTH()
			mysql> SELECT LENGTH(column1) FROM t1;
		--获取长度
		
		REPLACE()
			mysql> SELECT REPLACE(cloumn1，'A','B') FROM t1;
		--替换
		
		CONNECTION_ID(),USER(),VERSION(),
			mysql>  SELECT CONNECTION_ID(),USER(),VERSION();
		--连接ID，用户，版本
		
		LAST_INSERT_ID()
			mysql> SELECT LAST_INSERT_ID() FROM t1;
		--返回上一条修改的一组数据，第一个自增字段的值,若没有自增字段则为0.
		
		ROW_COUNT()
			mysql> SELECT ROW_COUNT();
		--返回上一条sql影响的行数，update，delete返回正数，insert返回负数，
		
		AVG(),COUNT(),MAX(),MIN(),SUM()
		--平均数，统计，最大数，最小数，和
		
		MD5();
		--信息摘要算法
		
	
	自定义函数
	--函数的针对性更强，只有一个返回值，可以灵活的嵌套sql语句
	
		--无参数
		
		创建：
				mysql> CREATE FUNCTION func1()
				RETURNS VARCHAR(255)
				RETURN DATE_FORMAT(NOW(),'%m/%d/%y');
					
		调用：
			mysql> SELECT func1();
			
		删除：
			mysql> DROP FUNCTION func1;
		查看：
			mysql> SHOW FUNCTION STATUS WHERE Db='t1'；
			
		--有参数
		
		创建：
		
				mysql> CREATE FUNCTION func2(num1 INT UNSIGNED,num2 INT UNSIGNED)
				RETURNS FLOAT(10，2) UNSIGNED
				RETURN (num1+num2)/2;
				
		调用：
				mysql> SELECT func2(column1,column2) FROM t1;
				
		--复合结构
		
			DELIMITER// --以//结尾，定义复合结构需要把结尾的符号修改，待定义完成后修改回来
			
			创建:
			
				mysql> CREATE FUNCTION func3(name VARCHAR(255))
				RETURNS INT UNSIGNED
				BEGIN
				INSERT INTO t1('ID') VALUES(name);
				RETURN LAST_INSERT_ID()
				END//
				

七：存储过程

--存储过程实现的功能复杂一些，可以返回多个值，一般独立运行来提高运行效率，且只需编译一次

	--无参数
	
		创建：
		
				mysql> CREATE PROCEDURE pro1()
				SELECT VERSION();
				
		调用：
		
				mysql> CALL pro1();
				mysql> CALL pro1;
 
		删除：
	
				mysql> DROP PROCEDURE pro1;
				
		查看：
		
				mysql> show PROCEDURE STATUS where Db='t1'
				
	--带参数
	
		创建：
				mysql> CREATE PROCEDURE pro2(IN num1 INT UNSIGNED)
				BEGIN
				DELETE FROM t1 WHERE column1=num1;
				END//
		
	--传递参数
	
		创建：

				mysql> CREATE PROCEDURE pro3(IN num1 INT UNSIGNED ,OUT num2 INT UNSIGNED)
				BEGIN
				DELETE FROM t1 WHERE column1=num1;
				SELECT COUNT(column1) FROM t1 INTO num2;
				END//

		调用： 
				mysql> CALL pro3(1，@num);
				mysql> SELECT @num;
				
			--声明：@a全局变量，@a局部变量，set @a：=1；select @a：=1；set可以不加：，select必须加
				set a=1;
				set a:=1;
				select @a:=1;
				
	--循环
	
		--WHILE

			mysql> drop PROCEDURE if EXISTS sum1;
			mysql> create procedure sum1(a int) 
			begin
				declare sum int default 0;  -- default 是指定该变量的默认值
				declare i int default 1;
			while i<=a DO -- 循环开始
			   set sum=sum+i;
			   set i=i+1;
			end while; -- 循环结束
			select sum;  -- 输出结果
			end	

		--LOOP

			mysql> drop PROCEDURE if EXISTS sum2;
			mysql> create procedure sum2(a int)
			begin
					declare sum int default 0;
					declare i int default 1;
					loop_name:loop -- 循环开始
						if i>a then 
							leave loop_name;  -- 判断条件成立则结束循环  好比java中的 boeak
						end if;
						set sum=sum+i;
						set i=i+1;
					end loop;  -- 循环结束
							select sum;
			end

		--REPEAT
		
			mysql> drop PROCEDURE if EXISTS sum3;
			mysql> create procedure sum3(a int)
			begin
				   declare sum int default 0;
				   declare i int default 1;
				   repeat -- 循环开始
						set sum=sum+i;
						set i=i+1;
				   until i>a end repeat; -- 循环结束
				   select sum; -- 输出结果
			end
			
		
八：触发器

	语法：
	
		CREATE TRIGGER(trigger_name)
		{BEFORE|AFTER}--设置为事前触发还是事后触发
		{INSERT|UPDATE|DELETE}--触发事件
		ON table_name--触发事件的表
		FOR EACH ROW--执行间隔
		body--触发sql
		
		--new表示新的数据，old表示旧的数据，insert只有new，delete只有old，update都有
		
		查看：
			mysql> SHOW TRIGGERS;
		
	实例：
	
		--INSERT 
		
			DROP TRIGGER IF EXISTS tri1;
			CREATE TRIGGER tri1
			AFTER INSERT ON tb1
			FOR EACH ROW
			BEGIN
				INSERT INTO tb2(id) VALUES(new.id);
			END;
	
		--DELETE
		
			DROP TRIGGER IF EXISTS tri2;
			CREATE TRIGGER tri2
			AFTER DELETE ON tb1
			FOR EACH ROW
			BEGIN
				DELETE FROM tb2 WHERE id=old.id;
			END;
			
		
九：系统管理
			
	权限管理
	--mysql数据库用来管理用户和权限，user表存储用户数据
	
		创建用户：
		
			mysql> CREATE user 'root1'@'localhost' IDENTIFIED by 'root'
			--无权限,连接之后只有information_schema表可以查看，@前后加不加''都可以
			--localhost换成%即是任意ip
			--防火墙要允许访问
		
		授予权限：
		
			mysql> GRANT SELECT ON fuliba.* TO root1@localhost
			mysql> GRANT ALL PRIVILEGES ON *.* TO 'Cshare'@'localhost' WITH GRANT OPTION;
			--详细的权限范围见参考【4】，create routine 创建function，procedure权限，alter routine则互补
			--WITH GRANT OPTION使授予者能接着创建用户
		
		撤销权限：
		
			mysql> REVOKE SELECT ON fuliba.* FROM root1@localhost
			
		刷新权限：
		
			mysql> FLUSH PRIVILEGES;
			--在授予或撤销某项特权以后，将从mysql数据库中的特权表中重新加载所有特权。
			
		查看权限：
		
			mysql> SHOW GRANTS FOR root1@localhost
			--查看某个用户的权限
			
		删除权限：
		
			mysql> DROP USER root2@localhost
			
		创建并赋予权限：
		
			语法：
			
			grant [权限list] on [d1.t1] to [username@hostname] identified by [password] with [options]
			--[]去掉直接可用，list以,分隔
			
			实例：
			
			mysql> GRANT ALL PRIVILEGES on *.* to 'root1'@'localhost' IDENTIFIED by 'root' With grant option
			mysql> GRANT ALL PRIVILEGES on *.* to 'xuniji'@'192.168.2.190' IDENTIFIED by 'root' With grant option
			--赋予root1所有的权限，赋予xuniji远程用户访问权

		8.0版本创建用户：
		
			
	日志管理
	
		创建日志
		
			my.ini配置文件(默认c盘安装)地址：C:\ProgramData\MySQL\MySQL Server 5.7
			--开启二进制日志
			
			修改my.ini文件步骤：
			--参考【5】
			
				剪切：C:\ProgramData\MySQL\MySQL Server 5.7\my.ini
				粘贴：D盘
				修改：my.ini文件,任选一种修改，推荐第二种指定日志目录
					# Binary Logging
					log-bin=mysql-bin
					binlog-format=Row
					
					# Binary Logging.
					log-bin=D:\mysql_log\mysql-bin
					binlog-format=Row
					--在D盘下新建一个mysql_log的文件夹

				打开管理员cmd界面
				copy "D:\my.ini" "C:\ProgramData\MySQL\MySQL Server 5.7"
				or 剪切回来
					
			查看：
			
				mysql> show variables like '%log_bin%';
				mysql> show binary logs
				--查看二进制文件，就是查看变量
				--查看具体的文件目录
				C:\ProgramData\MySQL\MySQL Server 5.7\Data
				--里面还有其他类型的日志
				
			添加：
			
				 mysql> FLUSH LOGS;
				 --产生新的日志文件
			
		日志恢复
		--数据库应定期备份，若在空窗期出现故障，可用二进制文件恢复，参考【5】
			
			通过时间恢复：
			
				cmd>>> mysqlbinlog mysql-bin.000001 --stop-date="2011-10-23 15:05:00"|mysql -uroot -proot)
				--cmd模式目录切换到日志所在目录(mysqlbinlog是mysql自带的日志管理工具，路径包含空格要""),时间大于故障点即可
				
			通过操作点恢复：
			
				cmd>>> mysqlbinlog D:\mysql_log\mysql-bin.000001 > D:\log.txt
				--以txt文档显示日志，查找编号
				cmd>>> mysqlbinlog mysql-bin.000001 --stop-pos=875 | mysql -uroot -p
				--恢复mysql-bin.000001文件的开始到875
				cmd>>> mysqlbinlog mysql-bin.000001 --start-pos=1008 | mysql -uroot -p mytest
				--恢复mysql-bin.000001文件1008编号到结束
			
			
十：SQL优化

	执行计划
	
		mysql> explain select ………
		--各参数解释见参考【3】，用来查看sql的执行计划，优化sql常用

	优化技巧：
	
		/*
		1.varchar()，int()的宽度可能小，尽量设置NOT NULL
		
		2.使用join替代子查询
		
		3.union代替手动创建的临时表
		
		4.使用事务保持所有的sql语句，要么全部执行，要么都不执行，当多个用户操作数据库时十分有效,事务使用begin，commit将sql包裹
			BEGIN;
			sql语句
			COMMIT;
			--能使用索引的时候，mysql会使用行锁，不能使用则用表锁
			
		5.锁定表
			LOCK TABLE t1 WRITE,t2 READ
			sql语句
			UNLOCK TABLES;
			--加读锁时，其他用户只能读不能写，加写锁时，其他用户被阻塞，直到获取到锁
			
		6.使用外键保证数据的完整性
		
		7.使用索引，索引避免建在重复值多的列，应建立在那些将用于JOIN,WHERE判断和ORDERBY排序的字段上
		  
		8.语句中应让相同类型的字段间进行比较的操作，在建有索引的字段上尽量不要使用函数进行操作，
		  在搜索字符型字段时，我们有时会使用LIKE关键字和通配符，这种做法虽然简单，但却也是以牺牲系统性能为代价的。
		  
		*/
			
十一：扩充

		set @a='0422';
		set @_sql=concat('select * from tableau.',@a);
		PREPARE stmt FROM @_sql;
		EXECUTE stmt ;
		DEALLOCATE PREPARE stmt;

	
	

/*参考：

来源：http://www.w3school.com.cn/sql/sql_top.asp	

【1】数据类型：http://www.w3school.com.cn/sql/sql_datatypes.asp
【2】date函数：http://www.w3school.com.cn/sql/sql_dates.asp
【3】执行计划：https://blog.csdn.net/heng_yan/article/details/78324176
【4】权限修改：http://www.cnblogs.com/snsdzjlz320/p/5764977.html
【5】开启二进制日志：http://www.cnblogs.com/wangwust/p/6433453.html
【6】恢复二进制日志：http://www.jb51.net/article/54333.htm
【7】外键约束：http://www.cnblogs.com/love_study/archive/2010/12/02/1894593.html
代理：
http://blog.csdn.net/xsjyahoo/article/details/51568712

*/