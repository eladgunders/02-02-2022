import threading
import time


class MyThread(threading.Thread):

    def __init__(self, threadID, jump):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.jump = jump

    def run(self):
        x = 0
        while True:
            if x > 30:
                break
            print(f'Thread {self.threadID}: {x}')
            x += self.jump
            time.sleep(1)

thread1 = MyThread('a', 1)
thread2 = MyThread('b', 2)
thread3 = MyThread('c', 3)

thread1.start()
thread2.start()
thread3.start()
