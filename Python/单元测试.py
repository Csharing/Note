class Dict(dict):

    def __init__(self, **kw):
        super(Dict,self).__init__(**kw)
        self.a=1
        print(self,self.a)
#super继承dict类

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
        

    def __setattr__(self, key, value):
        #设置属性值
        self[key] = value
