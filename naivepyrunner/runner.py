from time import sleep, time
from collections import deque
from enum import Enum
from threading import Thread

from .job import Job
from .task import Task
from .queue import Queue, DuetimeQueue
from .queuetransposer import QueueTransposer
from .worker import Worker, DedicatedWorker

class Runner(object):
    class Mode(Enum):
        SEQUENTIAL = 0
        SHARED = 1
        UNLIMITED = 2

    def __new__(cls, mode=None, *args, **kwargs):
        if mode is None:
            mode = Runner.Mode.SEQUENTIAL

        if mode is Runner.Mode.SHARED:
            return super().__new__(SharedQueueRunner, *args, **kwargs)
        elif mode == Runner.Mode.UNLIMITED:
            return super().__new__(UnlimitedRunner, *args, **kwargs)

        return super().__new__(SequentialRunner, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        self.queue = Queue()
        self.to_enqueue = Queue()
        self.running = False

    def add_task(self, task):
        if not isinstance(task, Task):
            raise Exception('task is not a Task but a '+str(type(task)))
        job = Job(
            task = task,
            duetime = time()
        )
        self.queue.insert(job)

    def run(self):
        pass

    def stop(self):
        self.running = False

class SequentialRunner(Runner):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.queue = DuetimeQueue()
        self.to_enqueue = None

    def run(self):
        self.running = True
        while self.running:
            job = self.queue.pop_if_due()

            if job and job.execute():
                self.queue.insert(job)

            if not job:
                sleep(0.01)

class SharedQueueRunner(Runner):
    def __init__(self, worker_pool_size=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not worker_pool_size:
            from multiprocessing import cpu_count
            worker_pool_size = cpu_count()

        self.tasks = DuetimeQueue()
        self.workers = [Worker() for i in worker_pool_size]
        self.transposer = QueueTransposer(source=kself.tasks, target=self.queue)

    def run(self):
        self.running = True
        self.transposer.start()
        for worker in self.workers:
            worker.start()
        self.transposer.run()

    def stop(self):
        super().stop()
        for worker in self.workers:
            worker.stop()
        self.transposer.stop()

class UnlimitedRunner(Runner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.to_enqueue = None
        self.queue = None
        self.threads = []

    def add_task(self, task):
        worker = DedicatedWorker(task)
        thread = Thread(target=worker.run)
        if self.running:
            thread.start()
        self.threads.append(thread)

    def run(self):
        self.running = True
        for thread in self.threads:
            thread.start()
        while self.running:
            sleep(0.1)

    def stop(self):
        for thread in self.threads:
            thread.join()
