#!/usr/bin/env python

from random import randint
from naivepyrunner import Runner
from helloworldhandler import HelloWorld

if __name__ == "__main__":
    runner = Runner(handler_threads=5, feeder_threads=1)
    for i in range(60):
        runner.add_handler(HelloWorld(hw=i, pause_center=randint(1,5)))
    runner.run()
