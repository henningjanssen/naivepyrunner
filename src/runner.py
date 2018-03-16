import threading
from time import time
from collections import deque

from pipeline import Pipeline
from task import Task

class Runner(object):
    def __init__(self, threads=-1, safe=True):
        self.pipes = []
        self.threads = []
        self.tasks = deque()
        self.unlimited = threads < 0
        self.running = False;
        self.thread_count = threads
        self._runner = None
        self.safe = safe

        if threads > 0:
            for i in range(threads):
                self.pipes.append(
                    Pipeline(safe)
                )
                self.threads.append(Thread(self._walk_pipeline(i)))

    def add_handler(self, handler):
        if not isinstance(handler, Handler):
            raise Exception('handler is not a Handler')
        task = Task(
            task = handler,
            duetime = time()
        )
        if self.unlimited:
            # create it immediately. faster than setting it frontside
            # of the deque because calculation-times can be omitted
            pipe = Pipeline(self.safe)
            pipe.push(task)
            self.pipes.append(task)
            thread = Thread(self._walk_pipeline(
                self.pipes.index(pipe)
            ))
            if self.running:
                thread.run()
            self.threads.append(thread)

        else:
            # wait for runner to list it somewhere
            self.tasks.append(task)

    def join(self):
        if self.running:
            self.stop()
        while self.threads:
            self.threads.pop().join()
        if self._runner:
            self._runner.join()

    def run(self, blocking=True):
        self.running = True
        for thread in self.threads:
            thread.run()

        if self.threads == 0:
            if blocking:
                self._run_single()
            else:
                self._runner = Thread(self._run_single())
                self._runner.run()

        else:
            if self.unlimited:
                self._run_unlimited()
            else:
                if blocking:
                    self._runner = Thread(self._run_limited())
                    self._runner.run()
                else:
                    self._run_limited()

    def stop():
        self.running = False
        for pipe in self.pipes:
            pipe.stop()

    def _calc_pipeno(self, task):
        min_delay = 0
        min_pos = 0
        min_index = 0
        for i in range(self.thread_count):
            (delay, pos) = pipe.optimal_position()
            if delay < min_delay:
                min_delay = delay
                min_pos = pos
                min_index = i
        self.pipes[min_index].push(task, min_pos)

    def _run_single(self):
        pipe = Pipeline(self.safe)
        while self.tasks:
            pipe.push(self.task.pop())

        for task in pipe.walk():
            pipe.push(task)
            while self.tasks:
                pipe.push(self.tasks.pop())

    def _run_limited(self):
        for i in self.thread_count:
            this.pipes.push(Pipeline())
            thread = Thread(self._walk_pipeline(i))
            thread.run()
            this.threads.push(thread)

        while self.running():
            if not self.tasks:
                sleep(0.4)
                continue
            task = self.tasks.pop()
            pipe_no = self._calc_pipeno(task)
            self.pipes[pipe_no].push(pipe_no)

    def _run_unlimited(self):
        while self.running():
            pipe_count = 0
            while tasks:
                pipe = Pipeline()
                pipe.push(self.tasks.pop())
                self.pipes.append(pipe)

                #start async func
                thread = Thread(self._walk_pipeline(pipe_count))
                pipe_count += 1
                thread.run()
                self.threads.append(thread)
            sleep(0.4)

    def _walk_pipeline(self, pipe_index):
        while self.running:
            self.tasks.appendLeft(self.pipes[pipe_index].walk())
