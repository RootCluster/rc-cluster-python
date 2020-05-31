import threading
import time
from threading import current_thread


# 多线程示例
def custom_thread(arg1, arg2):
    print(current_thread().getName(), 'start')
    print('%s %s' % (arg1, arg2))
    time.sleep(1)
    print(current_thread().getName(), 'stop')


for i in range(1, 5, 1):
    # ti = no_thread(i, i + 1)
    t2 = threading.Thread(target=custom_thread, args=(i, i + 1))
    t2.start()

print(current_thread().getName(), 'end')


# 重写 threading.Thread 的 run() 方法
class overwrite_run_thread(threading.Thread):
    def run(self) -> None:
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


thread1 = overwrite_run_thread()
thread1.start()
thread1.join()
print(current_thread().getName(), 'end')
