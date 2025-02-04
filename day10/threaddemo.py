import threading
import time

print("main task kill the enemy")
def call_backup():
    print("calling friend")
    time.sleep(1)
    print("friend went back to position")
def got_backup():
    time.sleep(1)
    print("Friend came for support")
    time.sleep(1)
    print("enemy eliminated")
def thread3():
    print("3rd thread started")
    time.
thread=threading.Thread(target=call_backup)
thread2=threading.Thread(target=got_backup)
thread.start()
thread2.start()
thread.join()

print("Got points")
