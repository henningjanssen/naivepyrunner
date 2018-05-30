from collections import deque
from threading import Lock
from time import time
import heapq

class Queue(object):
    def __init__(self, *args, **kwargs):
        self.queue = deque()
        self.lock = Lock()

    def insert(self, job):
        with self.lock:
            self.queue.append(job)

    def is_first_due(self):
        with self.lock:
            if self.queue:
                return self.queue[0].is_due()
            return False

    def pop(self):
        try:
            return self.queue.popleft()
        except IndexError:
            return None

    def pop_if_due(self):
        with self.lock:
            if self.queue and self.queue[0].is_due():
                return self.queue.popleft()
        return None

class DuetimeQueue(Queue):#
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue = []

    def insert(self, job):
        with self.lock:
            heapq.heappush(self.queue, (job.duetime, job))

    def pop(self):
        with self.lock:
            try:
                return heapq.heappop(self.queue)[1]
            except IndexError:
                return None

    def pop_if_due(self):
        with self.lock:
            if self.queue and self.queue[0][1].is_due():
                return heapq.heappop(self.queue)[1]
            return None

class TimeboxQueue(Queue):
    pass
