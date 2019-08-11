import threading

class Foo:
    def __init__(self):
        self.locks = (threading.Lock(), threading.Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.locks[0]:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.locks[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
