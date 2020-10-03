# standard imports
from concurrent.futures import ThreadPoolExecutor
import threading
import time

# 3rd party imports

# application imports


class FakeDatabase():

    def __init__(self):
        self.value = 0
        self._rlock = threading.RLock()
        self.NUM_ITERATIONS = 3

    def update(self, thread_name):
        """
        RLock (Reentrant Lock) can be acquired multiple times by the same thread.
        It will increment every time the thread acquires it, and decrement when released.
        """
        print(f'thread {thread_name} starting update')
        self._update(thread_name, self.NUM_ITERATIONS)
        print(f'thread {thread_name} ending update')

    def _update(self, thread_name, i):
        if i <= 0:
            return
        print(f'thread {thread_name} trying to get rlock')
        self._rlock.acquire()
        print(f'thread {thread_name} got the rlock')
        local_copy = self.value
        local_copy += 1
        self.value = local_copy

        # recursive call within the same thread, before releasing the lock
        self._update(thread_name, i - 1)

        print(f'thread {thread_name} releases the rlock')
        self._rlock.release()


fake_database = FakeDatabase()
print(f'starting db value = {fake_database.value}')

NUM_THREADS = 3

with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    executor.map(lambda x: fake_database.update(x), range(NUM_THREADS))
    executor.shutdown(wait=True)

print(f'ending db value = {fake_database.value}')
