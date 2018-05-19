#!/usr/bin/env python

from random import randint
from naivepyrunner import Runner
from helloworldtask import HelloWorld

if __name__ == "__main__":
    runner = Runner(mode=Runner.Mode.UNLIMITED)
    for i in range(60):
        runner.add_task(HelloWorld(randint(1, 30), i))
    runner.run()
