from .Collatz import test_excessive_pattern
from .seq_generator import generate
from multiprocessing import Process, Queue, Value, Pool


class Counter(object):

    def __init__(self):
        self.val = Value('i', 0)

    def increment(self, n=1):
        with self.val.get_lock():
            self.val.value += n

    @property
    def value(self):
        return self.val.value


def feeder_thread(queue, length):
    for i in generate("", "", 0, length):
        queue.put(i)


def worker(queue, counter):
    while True:
        if queue.empty() == True:
            break
        else:
            pattern = queue.get()
            if test_excessive_pattern(pattern) != None:
                counter.increment(2)
            else:
                counter.increment(1)


if __name__ == '__main__':
    # for leng in range(15,22):
    leng = 20
    c = Counter()
    queue = Queue(60000)
    writer = Process(target=feeder_thread, args=(queue, leng))
    writer.start()
    processes = [Process(target=worker, args=(queue, c)) for i in range(3)]
    for i in processes:
        i.daemon = True
        i.start()
    for i in processes:
        i.join()
    print((leng+1, c.value))
