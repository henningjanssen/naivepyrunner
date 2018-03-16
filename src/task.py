from time import time

class Task(object):
    def __init__(self, task, duetime):
        self.task = task
        self.duetime = duetime
        self.execution_times = []
        self.average_execution_time = 0
        self.probable_delay = 0

    def execute(self):
        start = time()
        self.duetime = self.task.execute()
        self.probable_delay = 0
        ex_time = time()-start
        if self.execution_times > 7:
            self.execution_times.remove(0)
        self.execution_times.append(ex_time)
        self.average_execution_time = sum(self.execution_times)
            / len(self.execution_times)
        return self
