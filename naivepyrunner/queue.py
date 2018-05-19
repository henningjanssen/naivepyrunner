from collections import deque
from threading import Lock
from time import time

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

class DuetimeQueue(Queue):
    def insert(self, job):
        with self.lock:
            queue_len = len(self.queue)
            now = time()

            if len(self.queue) == 0:
                self.queue.append(job)

            # naive approach to find the shorter side to start from
            elif (queue_len == 1
                or abs(self.queue[0].duetime - now) >
                    abs(self.queue[-1].duetime - now)
            ):
                self._insert_from_left(job)

            else:
                self._insert_from_right(job)

    def _insert_from_left(self, job):
        if self.queue[0].duetime > job.duetime:
            self.queue.appendleft(job)

        inserted = False
        for i in range(0, len(self.queue)-1):
            if (self.queue[i].duetime <= job.duetime
                    and self.queue[i+1].duetime > job.duetime):
                self.queue.insert(i+1, job)
                inserted = True
                break

        if not inserted:
            self.queue.append(job)

    def _insert_from_right(self, job):
        if self.queue[-1].duetime < job.duetime:
            self.queue.append(job)

        inserted = False
        for i in range(len(self.queue)-1, 0, -1):
            if (self.queue[i].duetime > job.duetime
                    and self.queue[i-1].duetime <= job.duetime):
                self.queue.insert(i, job)
                inserted = True
                break

        if not inserted:
            self.queue.appendleft(job)

class TimeboxQueue(object):
    pass
