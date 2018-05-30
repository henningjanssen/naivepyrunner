from time import sleep, time
from random import uniform

from naivepyrunner import Task

class HelloWorld(Task):
    def __init__(self, pause_center=0, hw = 0):
        self.pause_center = pause_center
        self.sleep_time = 0
        self.hw = hw
        self.last_execution = time()
        self._first = True

    def execute(self):
        now = time()
        wait = now - self.last_execution
        pause = (0 if self.pause_center == 0
            else max(uniform(self.pause_center-0.7, self.pause_center+0.7), 0)
        )
        print(
            'Hello World! hw: {hw}; time: {time}; le: {le};'
            ' sleep: {sleep}; wait: {wait}; pause={pause}; diff: {diff}'.format(
                hw = self.hw,
                time = now,
                le = -1 if self._first else self.last_execution,
                sleep = self.sleep_time,
                wait = wait,
                diff = wait - self.sleep_time,
                pause = pause
            )
        )
        self._first = False
        if self.pause_center != 0:
            sleep(pause)
        self.sleep_time = uniform(0, 30)
        self.last_execution = time()
        return self.sleep_time
