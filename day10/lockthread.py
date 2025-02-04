import threading
import time


def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has aquired the lock")
        time.sleep(2)
        print(f"{threading.current_thread().name} has released the lock")
lock=threading.Lock()
threads=[threading.Thread(target=task,args=(lock,))]