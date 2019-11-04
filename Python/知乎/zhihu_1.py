# -*-coding:utf-8-*-
__version__='3.6.2'

import requests
import time
import re
import json
import os,sys,subprocess
from PIL import Image

class zhihu():

    captcapfile=os.path.join(sys.path[0],'captcapfile.gif')
    cookiefile=os.path.join(sys.path[0],'cookie')

    def __init__(self):
        os.chdir(sys.path[0])
        self.session=requests.session()
        self.session.headers.update({
            'HOST': 'www.zhihu.com',
            'Referer': 'https://www.zhihu.com',
            'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
        })
        self.__cookie=self.loadcookie()
        if self.__cookie:
            print('\n使用已有Cookie登录……')
            self.session.cookies.update(self.__cookie)
        else :
            print('没找到Cookie文件，请使用login方法登录一遍！')



    def get_xsrf(self):
        home_url = 'https://www.zhihu.com'
        rel = r'[\s\S]*name="_xsrf" value="(.*?)"'
        response = self.session.get(home_url)
        find_xsrf = re.match(rel, response.text)
        #print(response.request.headers)
        return find_xsrf.group(1)



    def get_captcha(self):
        captcha_url = 'http://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn' % (int(time.time() * 1000))
        points = [[22.796875, 22], [42.796875, 22], [63.796875, 21], [84.796875, 20], [107.796875, 20],
                  [129.796875, 22], [150.796875, 22]]
        captcha = {'img_size': [200, 44],'input_points': []}
        response = self.session.get(captcha_url)
        with open(self.captcapfile, 'wb') as f:
            f.write(response.content)
        #try:
        #    img = Image.open(self.captcapfile)
        #    img.show()
        #    img.close()
        #except:
        #    pass
        
        subprocess.call(self.captcapfile, shell=True)
        seq = input('请输入:>>>')
        for i in seq:
            captcha['input_points'].append(points[int(i) - 1])
        os.remove(self.captcapfile)
        return json.dumps(captcha)


    def login(self,user, word):
        post_url = 'https://www.zhihu.com/login/phone_num'
        post_data = {
            'captcha_type': 'cn',
            '_xsrf': self.get_xsrf(),
            'phone_num': user,
            'password': word,
            'captcha': self.get_captcha(),
        }
        response = self.session.post(post_url, data=post_data)
        response = json.loads(response.text)
        print(response['msg'])
        if response['msg']=='登录成功':
            self.savecookie()


    def savecookie(self):
        with open(self.cookiefile,'w') as f:
            cookie=self.session.cookies.get_dict()
            json.dump(cookie,f)
        print('已生成Cookie文件：',self.cookiefile)


    def loadcookie(self):
        if os.path.exists(self.cookiefile):
            with open(self.cookiefile,'r') as f:
                cookie=json.load(f)
            return cookie
        return None



if __name__=='__main__':
    test=zhihu()
    test.login('13006146654','1193543051')
    params = {'type': 'content', 'q': '爱情'}
    response=test.session.get('https://www.zhihu.com/search',params=params,timeout=10)
    #print(response.request.headers)
    print(response.text)
