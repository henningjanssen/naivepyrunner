from random import randint
from time import time

from ..src import Handler, Runner

class HelloWorld(Handler):
    def __init__(self, sleep_time = 10, hw = 0):
        self.sleep_time = sleep_time
        self.hw = hw
        self.last_execution = -1

    def execute(self):
        now = time()
        wait = now-self.last_execution
        print(
            'Hello World! hw: {hw}; time: {time}; le: {lw};'
            ' sleep: {sleep}; wait: {wait}; diff: {diff}'.format({
                hw: self.hw,
                time: time,
                le: self.last_execution,
                sleep: self.sleep_time,
                wait: wait,
                diff: wait - self.sleep_time
            })
        )
        return self.sleep_time

if __name__ == "__main__":
    runner = Runner(threads=3)
    for i in range(30):
        runner.add_handler(HelloWorld(randint(1, 30), i))
    runner.run()
