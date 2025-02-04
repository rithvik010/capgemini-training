import threading
import queue

def producer(q):
    for i in range(10):
        print("produced b    :",i)
        q.put(i)
def consumer(q):
    while True:
        item=q.get()
        if item==None:
            break
        print("consumed:",item)
def main():
    q=queue.Queue()
    producer_thread=threading.Thread(target=producer,args=(q,))

    consumer_thread=threading.Thread(target=consumer,args=(q,)) 
    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    q.put(None)
    consumer_thread.join()
    print("Thread commiunication completed")
main()