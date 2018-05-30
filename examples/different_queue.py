#!/usr/bin/env python

from random import randint
from naivepyrunner import Runner, QueueMode
from helloworldtask import HelloWorld

if __name__ == "__main__":
    runner = Runner(mode=Runner.Mode.SHARED_QUEUE, queue_mode=QueueMode.FIFO)
    for i in range(60):
        runner.add_task(HelloWorld(hw=i, pause_center=randint(1,5)))
    runner.run()
