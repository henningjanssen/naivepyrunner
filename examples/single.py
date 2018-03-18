#!/usr/bin/env python

from random import randint
from naivepyrunner import Runner
from helloworldhandler import HelloWorld

if __name__ == "__main__":
    runner = Runner(handler_threads=0, feeder_threads=0)
    for i in range(10):
        runner.add_handler(HelloWorld(hw=i, pause_center=randint(0, 5)))
    runner.run()
