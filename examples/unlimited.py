#!/usr/bin/env python

from random import randint
from naivepyrunner import Runner
from helloworldhandler import HelloWorld

if __name__ == "__main__":
    runner = Runner(handler_threads=-1, feeder_threads=0)
    for i in range(60):
        runner.add_handler(HelloWorld(randint(1, 30), i))
    runner.run()
