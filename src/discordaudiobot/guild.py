from queue import Queue


class Guild:
    id: int
    queue: Queue

    def __init__(self, _id: int) -> None:
        self.id = _id
        self.queue = Queue()

    def add_to_queue(self, link: str) -> None:
        self.queue.put(link)

    def pop(self) -> None:
        return self.queue.get()
