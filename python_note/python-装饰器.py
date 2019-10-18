def get_a(*args,**kwargs):
    def get_func(func):
        def get_b(*args,**kwargs):
            func(*args,**kwargs)
            return 'func'
        return get_b
    print(*args,**kwargs)

    return get_func

##装饰器对函数的赋值级别比init高
##一层层就内部函数作为对象暴露出来

a=get_a('a')
@a
def abc():
    pass
print(abc())

[Running] python -u "c:\Users\Cshare\Desktop\Note\python_note\python-装饰器.py"
a
func