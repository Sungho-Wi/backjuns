class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return " ".join(map(str, self.queue))

    def put(self, item):
        self.queue.append(item)

    def get(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop()


if __name__ == "__main__":
    queue = Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)

    print("현재 queue")
    print(queue)

    while queue:
        item = queue.get()
        if item is None:
            break
        print("POP > {}".format(item))