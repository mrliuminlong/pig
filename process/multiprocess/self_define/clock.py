#自定义类　功能间隔显示当前时间　共显示5次
from multiprocessing import Process
import time

class ClockProcess(Process):
    def __init__(self, value):
        self.value = value
        super().__init__()
    #重写run方法
    def run(self):
        for i in range(5):
            print("Now time is ",time.ctime())
            time.sleep(self.value)

#创建自定义类进程对象
p = ClockProcess(2)
p.start()
p.join()
