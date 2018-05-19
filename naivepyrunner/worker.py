from time import sleep
from collections import deque
from queue import Queue

# For DedicatedWorker
from threading import Lock

from .task import Task

class Worker(object):
    def __init__(self, queue=None, tasks=None, *args, **kwargs):
        self.running = False
        self.queue = queue if queue else Queue()
        self.tasks = tasks if tasks else Queue()

    def run(self):
        self.running = True
        while self.running:
            self.step()

    def step(self):
        def step(self):
            job = None
            with self.queue.lock():
                if self.queue.is_first_due():
                    job = self.queue().pop()

            if job and job.execute():
                self.tasks.insert(job)

    def stop(self):
        self.running = False

class DedicatedWorker(Worker):
    def __init__(self, task, *args, **kwargs):
        self.task = task
        self.lock = Lock()
        self.running = False
        self.timer = None

    def run(self):
        self.running = True
        while self.running:
            sleep(0.1)

    def step(self):
        with self.lock.acquire():
            sleep_time = self.task.execute()
            if sleep_time >= 0:
                self.timer = Timer(sleep_time, self.step)

    def stop(self):
        if self.lock.acquire(blocking=False):
            self.running = False
            if self.timer:
                self.timer.cancel()
            self.lock.release()
        else:
            self.task.stop()
