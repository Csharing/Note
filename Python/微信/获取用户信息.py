import requests
import json
data={'corpid':'wwd72a723ba184cb5e',
      'corpsecret':'tXLKAsMBYsk8fiuVYVGSI38V7xTj2yrjXaAa6Ewgvpg'
}
url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
repose=requests.get(url=url,params=data)
#print(repose.text)
access_token=repose.json()['access_token']
print(access_token)
par={'access_token':access_token,
     'userid':'chengpan'
}
acce='https://qyapi.weixin.qq.com/cgi-bin/user/get'
a=requests.get(url=acce,params=par).text
print(a)
