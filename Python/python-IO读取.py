# with open(r"C:\Users\HaSEE\Desktop\lilianjie.txt",'r',encoding='utf-8')as f:
#     print(f.read())
    # for t in f.readlines():
    #     print(t.strip())
    #strip()把末尾的'\n'删掉

    # print(f.read(20))
    # print(f.read(20))
#open 的读取模式：
    # r 只读存在的文件
    # w 写模式，若文件不存在则创建，若存在则清空
    # a 写模式，若文件不存在则创建，若存在则续尾
    # r+ r模式的升级，可以进行写操作
    # w+ w模式的升级，可以进行读操作
    # a+ a模式的升级，可以进行读操作
    # b 二进制模式，图片视频等需要加上这个模式

'StringIO内存中读取数据'
from io import StringIO
# f=StringIO()
# f.write("hello")
# f.write("job")
# print(f.getvalue())
# a=StringIO()
# a.write("sds")
# print(a.getvalue())

# b=StringIO("Hello!\nHi\nGood!")
# while True:
#     strb=b.readline().strip()
#     if strb=='':
#         break
#     print(strb)
#readline只能一行行的读取数据

'BytesIO操作二进制数据，用法同StringIO'
from io import BytesIO
# c=BytesIO()
# c.write('中'.encode('Utf-8'))
# print(c.getvalue())
#
# d=BytesIO(b'\xe4\xb8\xad')
# print(d.read())


'操作文件和目录 os和os.path模块'
import os
# os.name #返回操作系统的类型，nt表示是window系统
# os.environ#返回操作系统中的所有环境变量
# os.environ.get('PATH')#返回PATH环境变量
#print(os.path.abspath('.'))#返回当前目录的绝对路径C:\Users\yq\Desktop\lead
#print(os.path.join(r'C:\Users\yq\Desktop\lead','测试'))#拼接路径C:\Users\yq\Desktop\lead\测试
#os.mkdir(r'C:\Users\yq\Desktop\lead\测试')#创建文件夹
#os.rmdir(r'C:\Users\yq\Desktop\lead\测试')#删除文件夹
#print(os.path.split(r'C:\Users\yq\Desktop\lead\测试.txt'))#拆分字符串('C:\\Users\\yq\\Desktop\\lead', '测试.txt')
#print(os.path.splitext(r'C:\Users\yq\Desktop\lead\测试.txt'))#拆分字符串('C:\\Users\\yq\\Desktop\\lead\\测试', '.txt')
#os.rename('ceshi.txt','ceshi.py')#重命名，不存在时会报错
#os.remove('ceshi.py')#删除文件
#shutil模块提供了copyfile()来复制文件

'序列化pickle,json模块'
import pickle
#d=dict(name='a',age='b')
#print(pickle.dumps(d))
# with open('test.txt','wb')as f:
#     pickle.dump(d,f)

#print(pickle.loads(b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x01\x00\x00\x00aq\x02X\x03\x00\x00\x00ageq\x03X\x01\x00\x00\x00bq\x04u.'))
# with open('test.txt','rb')as f:
#     dictf=pickle.load(f)
#     print(dictf)

import json
d=dict(name='a',age='b')
# print(json.dumps(d))
# with open('test1.txt','w')as f:
#     json.dump(d,f)

# print(json.loads('{"name": "a)", "age": "b"}')
# with open('test1.txt','r') as f:
#     dictf=json.load(f)
#     print(dictf)
#json 如果要序列化对象，则需要借助转换函数返回一个字典，和实例化一个对象

