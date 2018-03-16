from time import sleep, time

from task import Task

class Pipeline(object):
    def __init__(self, safe):
        self.walking = False
        self.tasks = []
        self.task_count = 0 # faster than len()
        self.expected_duration = 0
        self.probable_delay = 0
        self._delays
        self._delay_time

    def walk(self):
        self.walking = True
        while self.walking:
            if not self.tasks:
                self.expected_duration += 0.5
                sleep(0.5)
                self.expected_duration -= 0.5
                yield None

            if tasks[0].duetime <= time():
                task = self.tasks.pop(0)
                dur = task.average_execution_time
                sleep_time = task.execute()
                task.duetime = time()+sleep_time
                self.task_count -= 1
                self.expected_duration -= dur
                yield task

            if self.tasks:
                diff = time() - tasks[0].duetime
                if diff == 0:
                    continue
                else:
                    if self.save:
                        self.expected_duration += 0.5
                        sleep(0.5)
                        self.expected_duration -= 0.5
                    else:
                        self.expected_duration += diff
                        sleep(diff)
                        self.expected_duration -= diff

    def push(self, task, position=-1):
        if not isinstance(task, Task):
            raise InvalidArgumentException('task is not a Task')

        if position >= self.task_count:
            self.tasks.append(task)

        if position < 0:
            task.probable_delay = self.tasks
                ?self._calc_probable_delay(self.tasks[-1], task)
                :0
            self.tasks.append(task)
        else:
            self.tasks.insert(task, position)  # slower than append
            for i in range(max(position, 1), self.task_count+1):
                self.tasks[i].probable_delay = self._calc_probable_delay(
                    self.tasks[i-1],
                    self.tasks[i]
                )
        self.task_count += 1
        self.expected_duration += tasks.average_execution_time

    def optimal_position(self, task):
        tasks = self.tasks
        if not tasks:
            return (0, 0)

        min_delay = 0
        min_pos = self.task_count
        task_count = len(tasks)
        if time() - self._delay_time > 2:
            i_del = 0
            self._delays[:] = []
            self._delays[0] = 0
            for i in range(1, task_count):
                self._delays[i] = self._delays[i-1]
                    + self._calc_probable_delay(
                        tasks[i-1], tasks[i]
                    )

        min_delay = self._calc_probable_delay(tasks[-1], task)
        min_pos = -1
        for i in range(task_count, 0, -1):
            new_del = self._calc_full_delay(task, tasks[i-1:])
            if new_del < min_delay:
                min_delay = new_del
                min_pos = i
        return (min_delay, min_pos) # delay, position

    def _calc_full_delay(self, task, task_list):
        delay = self._calc_probable_delay(task_list[0], task)
        if len(tasks_list) > 1:
             last_delay = self._calc_probable_delay(task, task_list[1], delay)
             delay += last_delay

        for i in range(1, task_list-1):
            last_delay = self._calc_probable_delay(
                task_list[i],
                task_list[i+1],
                last_delay - task_list[i].probable_delay
            )
            delay += add_delay
        return delay

    def _calc_probable_delay(self, prev, task, adjustments=0):
        return prev.duetime
            + prev.probable_delay
            + prev.average_execution_time
            + adjustments
            - task.duetime
