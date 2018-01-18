class fib():
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        # a, b = 1, 1
        # for x in range(n):
        #     a, b = b, a + b
        # return a
        print(n.start,n.stop,n.step)
        return 'hah'

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)

    def __getattr__(self, item):
        return  'no'

    def __call__(self, *args, **kwargs):
        return 'call'

print(fib()[4:5:2])

fib()['a']='b'

del fib()['a']

print(fib().sdds)

print(fib()())
# for n in fib():
#     print(n)



class pro(object):

    @property
    def html(self):
        return self.a

    @html.setter
    def html(self,a):
        self.a=a

k=pro()

k.html='aaa'

print(k.html)