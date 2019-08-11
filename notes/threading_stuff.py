# Barrier sets up a count of threads that waits together until the count is reached..
# To define a barrier object, “threading. Barrier” is used.
# threading.Barrier(parties, action = None, timeout = None)
# Where,
# parties = Number of threads
# action = called by one of the threads when they are released.
# timeout = Default timeout value. In case no timeout value is specified for the wait(), this timeout value is used.

import time
import random
import threading

#
# def f1(b):
#     time.sleep(random.randint(2, 10))
#     print("{} woke at: {}".format(threading.current_thread().getName(), time.ctime()))
#     b.wait()
#     print("{} passed the barrier at: {}\n".format(threading.current_thread().getName(), time.ctime()))
#
#
# barrier = threading.Barrier(3)
# for i in range(3):
#     t = threading.Thread(target=f1, args=(barrier,))
#     t.start()


# Thread-2 woke at: Sun May 20 11:59:16 2018
# Thread-3 woke at: Sun May 20 11:59:21 2018
# Thread-1 woke at: Sun May 20 11:59:22 2018
# Thread-1 passed the barrier at: Sun May 20 11:59:22 2018
# Thread-2 passed the barrier at: Sun May 20 11:59:22 2018
# Thread-3 passed the barrier at: Sun May 20 11:59:22 2018

#
# def f2a():
#     time.sleep(random.randint(5, 7))
#     locks[0].release()
#     print("{} passed the lockA at: {}\n".format(threading.current_thread().getName(), time.ctime()))
#
#
# def f2b():
#     with locks[0]:
#         time.sleep(random.randint(2, 5))
#         print("{} passed the lockB at: {}\n".format(threading.current_thread().getName(), time.ctime()))
#         locks[1].release()
#
#
# def f2c():
#     with locks[1]:
#         time.sleep(random.randint(1, 3))
#         print("{} passed the lockC at: {}\n".format(threading.current_thread().getName(), time.ctime()))
#
#
# locks = (threading.Lock(), threading.Lock(), threading.Lock())
#
# locks[0].acquire()
# locks[1].acquire()
# locks[2].acquire()
# t1 = threading.Thread(target=f2a)
# t1.start()
# t2 = threading.Thread(target=f2b)
# t2.start()
# t3 = threading.Thread(target=f2c)
# t3.start()

# Thread-1 passed the lockA at: Fri Aug  9 21:07:20 2019
# Thread-2 passed the lockB at: Fri Aug  9 21:07:22 2019
# Thread-3 passed the lockC at: Fri Aug  9 21:07:25 2019

#
# def f3a():
#     time.sleep(random.randint(5, 7))
#     print("{} passed the eventA at: {}\n".format(threading.current_thread().getName(), time.ctime()))
#     events[0].set()
#
#
# def f3b():
#     events[0].wait()
#     time.sleep(random.randint(2, 5))
#     print("{} passed the eventB at: {}\n".format(threading.current_thread().getName(), time.ctime()))
#     events[1].set()
#
#
# def f3c():
#     events[1].wait()
#     time.sleep(random.randint(1, 3))
#     print("{} passed the eventC at: {}\n".format(threading.current_thread().getName(), time.ctime()))
#
#
# events = (threading.Event(), threading.Event())
# t1 = threading.Thread(target=f3c)
# t1.start()
# t2 = threading.Thread(target=f3b)
# t2.start()
# t3 = threading.Thread(target=f3a)
# t3.start()

# Thread-3 passed the lockA at: Fri Aug  9 22:21:16 2019
# Thread-2 passed the lockB at: Fri Aug  9 22:21:21 2019
# Thread-1 passed the lockC at: Fri Aug  9 22:21:22 2019


# note the difference between lock and event.  If you wait on an event, the execution stalls until event.set() happens
# acquiring a lock only stalls if the lock is already required.
# Also, an event can have many waiters and when the lock is released, all of the waiters will wake up.
# A lock can have many waiters and when the lock is released, only one waiter will wake up and acquire the lock



def f4a():
    with condition:
        time.sleep(random.randint(5, 7))
        print("{} passed the eventA at: {}\n".format(threading.current_thread().getName(), time.ctime()))
        global order_value
        order_value = 1
        condition.notify(2)
        print("{} passed the eventA-2 at: {}\n".format(threading.current_thread().getName(), time.ctime()))


def f4b():
    with condition:
        condition.wait_for(first_finish)
        time.sleep(random.randint(2, 5))
        print("{} passed the eventB at: {}\n".format(threading.current_thread().getName(), time.ctime()))
        global order_value
        order_value = 2
        condition.notify()
        print("{} passed the eventB-2 at: {}\n".format(threading.current_thread().getName(), time.ctime()))


def f4c():
    with condition:
        condition.wait_for(second_finish)
        time.sleep(random.randint(1, 3))
        print("{} passed the eventC at: {}\n".format(threading.current_thread().getName(), time.ctime()))

        print("{} passed the eventC-2 at: {}\n".format(threading.current_thread().getName(), time.ctime()))

condition = threading.Condition()
order_value = 0
first_finish = lambda: order_value == 1
second_finish = lambda: order_value == 2
t1 = threading.Thread(target=f4c)
t1.start()
t2 = threading.Thread(target=f4b)
t2.start()
t3 = threading.Thread(target=f4a)
t3.start()


# you use a Condition when threads are interested in waiting for something to become true, and once its true, to have exclusive access to some shared resource.
#
# Whereas you use an Event when threads are just interested in waiting for something to become true.
#
# In essence, Condition is an abstracted Event + Lock, but it gets more interesting when you consider that you can have
# several different Conditions over the same underlying lock. Thus you could have different Conditions describing the state
# of the underlying resource meaning you can wake workers that are only interested in particular states of the shared resource.
