import urllib.request
import json
import sys
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s: %(message)s')

class wechat:
    def __init__(self):
        corpid = 'wwd72a723ba184cb5e'
        corpsecret = 'tXLKAsMBYsk8fiuVYVGSI38V7xTj2yrjXaAa6Ewgvpg'
        url = 'https://qyapi.weixin.qq.com'
        token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (url, corpid, corpsecret)
        self.token = json.loads(urllib.request.urlopen(token_url).read().decode('utf-8'))['access_token']
        self.url=url
        #print(url)
    def send_message(self,data):
        send_url = '%s/cgi-bin/message/send?access_token=%s' % (self.url, self.token)
        respone = urllib.request.urlopen(urllib.request.Request(url=send_url, data=data)).read()
        x=json.loads(respone.decode('utf-8'))['errcode']
        if x==0:
            logging.debug('Successfully %s' % self.subject)
            return 'Succesfully'
        else:
            logging.debug('Failed %s' % self.subject)
            return 'Failed'
    def messages(self,subject):
        self.subject=subject
        values = {
            "touser": '@all',
            "msgtype": 'text',
            "agentid": '1000004',
            "text": {'content':  subject},
            "safe": 0
        }
        data=bytes(json.dumps(values), 'utf-8')
        return self.send_message(data)
if __name__ == '__main__':
    a='1233'
    obj = wechat()
    ret = obj.messages(a)

