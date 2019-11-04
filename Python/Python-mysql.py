import pymysql.cursors
connection=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='1193543051',db='fuliba',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
cursor=connection.cursor()
f="dsggh"
a=str(4)
b="'"+f+"'"
c='"dfdf"'
d=str(4)
e='"jpg"'
#sql="INSERT INTO urls(page_id,page_url,img_url,img_id,jiforjpg) values("+str(a)+","+b+","+c+","+str(d)+","+e+")"
sql="INSERT INTO urls(page_id,page_url,img_url,img_id,jiforjpg) values(%s,%s,%s,%s,%s)"%(a,b,c,d,e)
print(sql)
cursor.execute(sql)
connection.commit()
connection.close()
print('done')

