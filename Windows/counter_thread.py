import threading


class CounterThread(threading.Thread):
    def __init__(self, flag, *args, **kwargs):
        super(CounterThread, self).__init__(*args, **kwargs)
        self.flag = flag
        self.__stop_event = threading.Event()

    def stop(self):
        self.__stop_event.set()

    def stopped(self):
        return self.__stop_event.is_set()

