import psutil
import sched
import time
import os
schedule_enter =sched.scheduler (time.time, time.sleep)

def task():
    print("run time: {}".format(int(time.time())))

def recycle_eval(c, inc):
    schedule_enter.enter( inc,0,recycle_eval,(c,inc))
    # os.system(c)
    task()

if __name__ == "__main__":
    inc = 3

    recycle_eval(int(time.time()), inc)
    schedule_enter.run()
    # print("A:%2f MB"%(psutil.Process(os.getpid()).memory_info().rss/1024/1024))