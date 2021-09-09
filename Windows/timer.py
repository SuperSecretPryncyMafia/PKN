import time

class Timer:
    def __init__(self, mins: int, secs: int):
        self.secs = secs
        self.mins = mins
        div = int(secs/60)
        self.mins += div
        
        if div:
            self.secs = int(secs/(60*div))

        self.timer =  "{}:{:02d}".format(self.mins, self.secs)
        self.timer_update()

    @classmethod
    def only_seconds(cls, secs: int):
        return cls(0, secs)

    def start_time(self):
        while self.mins + self.secs > 0:
            self.decrease_one_second()
            self.timer_update()

    def decrease_one_second(self):
        if self.secs > 0:
            time.sleep(1)
            self.secs -= 1
        elif self.mins > 0:
            self.mins -= 1
            self.secs = 59

    def timer_update(self):
        self.timer =  "{}:{:02d}".format(self.mins, self.secs)

    def return_time(self):
        return(self.timer)

