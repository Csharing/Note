# -*-coding:utf-8-*-
# -*-version:3.6.2-*-


"session的失败案例"



import requests,re,time,json
from PIL import Image

class zhihu(object):
    def __init__(self):
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Host':'www.zhihu.com',
           # 'Origin':'https://www.zhihu.com',
            'Referer':'https://www.zhihu.com',
        }



    def number_login(self,number,password):
        session = requests.session()

        response_xsrf=session.get('https://www.zhihu.com',headers=self.headers)
        match_obj = re.match('[\s\S]*name="_xsrf" value="(.*?)"', response_xsrf.text)
        self._xsrf=match_obj.group(1)

        captcha_url='https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn' % (int(time.time() * 1000))
        response_captcha=session.get(captcha_url,headers=self.headers)
        with open('captcha.gif','wb') as f:
            f.write(response_captcha.content)
        try:
            img=Image.open('captcha.gif')
            img.show()
            img.close()
        except:
            pass
        captcha={
            'img_siza':[200,44],
            'input_points':[],
        }
        points=[[22.796875, 22], [42.796875, 22], [63.796875, 21], [84.796875, 20], [107.796875, 20], [129.796875, 22],
              [150.796875, 22]]
        num=input('输入倒立字数字：\n')
        for i in num:
            captcha['input_points'].append(points[int(i)-1])
        self.get_captcha=json.dumps(captcha)

        post_url='https://www.zhihu.com/login/phone_num'
        post_data={
            'captcha_type':'cn',
            '_xsrf': self._xsrf,
            'phone_num':number,
            'password':password,
            'captcha':self.get_captcha,

        }
        # a=self._xsrf
        # if len(a)<70:
        #     post_data['captcha']=self.get_captcha
        response_text=session.post(post_url, data=post_data, headers=self.headers)
        # response_text = json.loads(response_text.text)
        print(response_text.text)

a=zhihu()
a.number_login('13006146654','1193543051')
