#!/usr/bin/env python

from random import randint
from naivepyrunner import Runner
from helloworldtask import HelloWorld

if __name__ == "__main__":
    runner = Runner(mode=Runner.Mode.SEQUENTIAL)
    for i in range(10):
        runner.add_task(HelloWorld(hw=i, pause_center=randint(0, 5)))
    runner.run()
