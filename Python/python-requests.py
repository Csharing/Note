# -*-coding:utf-8-*-
import requests
from PIL import  Image
from io import BytesIO
import ssl
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)#关闭验证证书的时候会出现警告



import json
# r=requests.get('https://api.github.com/events')
# print(r.json)
'速度'
# r=requests.get('https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=1447655050,2792058441&fm=173&s=15B07E941441BB5B5199CD0D030000D3&w=640&h=335&img.GIF',stream=True)
#print(r.text)
# print(r.url)#获取拼接的url
# print(r.encoding)#获取编码
# print(r.content)#获取头部

# i = Image.open(BytesIO(r.content))
# #可以利用PIL模块对下载的图片作处理，Byteio用来读取二进制数据
# print(type(i))
# i.save('a.gif','gif')

# print(r.raw)
# print(r.raw.read(10))
# r=requests.get('http://www.zjxc.com/forum.php?mod=forumdisplay&fid=97&filter=author&orderby=dateline',timeout=2)#1秒之后停止等待响应
#
# print(r.status_code)#响应码
# print(r.headers)
# r.status_code=requests.codes.ok#用内置的状态码判断
# r.raise_for_status()#与状态码一起使用，若服务器返回一个错误码，可以通过这个方法向程序抛出一个异常，若200，返回none
# print(r.headers)#返回响应头，以字典形式
# print(r.headers['Date'])
#print(r.cookies['example_cookie_name'])#找到响应的key
# print(r.history)

# headers={'User-Agent':'Bob'}
# r=requests.get('http://www.baidu.com/s',params={'wd':'Python'},headers=headers)#百度搜索结果展示
# print(r.status_code)
# print(r.url)
# print(r.text)
# print(r.request.headers)

# url='http://ip.taobao.com/service/getIpInfo.php'
# tryprint(r.request.headers):
#     r=requests.get(url,params={'ip':'8.8.8.8'},timeout=2)
#     r.raise_for_status()#如果不是200则会出错
# except requests.RequestException as e:
#     print(e)
# else:
#     res=r.json()
#     print(type(res),res,sep='\n')
# print(r.request.headers)


# headers={
#     'Accept-Encoding':'gzip, deflate, br',
#     'Accept-Language':'zh-CN,zh;q=0.8',
#     'Cache-Control':'max-age=0',
#     'Connection':'keep-alive',
#     'Host':'weibo.com',
#     'Referer':'https://weibo.com/',
#     'Upgrade-Insecure-Requests':'1',
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Cookie':'_s_tentry=-; Apache=7352751187873.278.1498524754273; httpsupgrade_ab=SSL; SINAGLOBAL=7352751187873.278.1498524754273; ULV=1508477720984:1:1:1:7352751187873.278.1498524754273:; login_sid_t=db1eb32d331fce3df9694a0bd99cd691; cross_origin_proto=SSL; UOR=df.joyoww.com,weibo.com,login.sina.com.cn; SSOLoginState=1508487209; SCF=Alyujz3hmB5hT1FSi8JqxoAbqvdezY5e2W0p_a7Db5ww-04nLj54AlAHAHZHadFhcuD-Kvk9zHu87J8JMmVohpM.; SUB=_2A2507cB5DeRhGeVH6VsS9CvNzjiIHXVXmraxrDV8PUNbmtBeLUfZkW9Gq5FGbrEQuMV4JY_xgO6a_VQ4pw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Qu9HTfWxz3a8Dz78OM8ZB5JpX5K2hUgL.Foe4eo.0Sh-pSKB2dJLoIX.LxK-L1hMLBo.LxK-L1hMLBonLxKqL1-zLB.eLxKML1hnLBo2LxK-L1K5L1he_i--fi-z7iKysi--ciKn7i-8Wi--fiKnfi-i2; SUHB=0jBI9lyYSFj0_q; ALF=1540023208; un=13006146654; wvr=6',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
# }
# r=requests.get('https://weibo.com/u/3929345154/home?wvr=5',headers=headers,verify=False)#verify关闭证书认证
# print(r.text)#新浪微博主页抓取

