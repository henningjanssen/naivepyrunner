from time import sleep

class QueueTransposer(object):
    def __init__(self, source, target, *args, **kwargs):
        self.source = source
        self.target = target
        self.running = False

    def run(self):
        while self.running:
            self.transpose_all()
            sleep(0.1)

    def transpose_all():
        while True:
            element = self.source.pop
            if not element:
                break
            self.target.insert(element)

    def transpose(self):
        element = self.source.pop()
        if element:
            self.target.insert(element)

    def stop(self):
        self.running = False
