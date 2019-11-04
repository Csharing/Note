# from threading import Thread
# from queue import Queue
# from time import sleep
# #q是任务队列
# #NUM是并发线程总数
# #JOBS是有多少任务
# q = Queue()
# NUM = 2
# JOBS = 10
# #具体的处理函数，负责处理单个任务
# def do_somthing_using(arguments):
#     print(arguments)
# #这个是工作进程，负责不断从队列取数据并处理
# def working():
#     while True:
#         if q.empty:
#             print('working')
#         arguments = q.get()
#         do_somthing_using(arguments)
#         #sleep(1)#当q为空时，q.get()会出错，这一句不执行，有时会出现"kong1'2 "同时打印的情况
#         q.task_done()#告诉队列这个数据被消费了，防止数据没有被使用
# #fork NUM个线程等待队列
# for i in range(NUM):
#     if q.empty:
#         print('NUM')
#     t = Thread(target=working)
#     t.setDaemon(True)#主线程结束时分线程随之结束
#     t.start()
#     #t.join()
#
# #等待所有JOBS完成
# for i in range(JOBS):
#     q.put(i)
# #把JOBS排入队列
# q.join()#等到队列为空，再执行下面的语句
# t.terminate()
# t.join()#用于阻塞主进程，等待子进程执行完再执行主进程
# print('a')

'GIL锁使得n个线程最多只能占用一个CPU，若要跑满则需要使用进程'
# import threading, multiprocessing
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

'ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等'
import threading
# 创建全局ThreadLocal对象:
local_school = threading.local()
def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()
t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

'线程锁，当多个线程需要修改同一个变量时，只有拥有线程锁的线程才能修改'
balance = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()