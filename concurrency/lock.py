# standard imports
from concurrent.futures import ThreadPoolExecutor
import threading
import time

# 3rd party imports

# application imports


class FakeDatabase():

    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, thread_name):

        """
        Only 1 thread should be executing below code at a time.
        This can be achieved by using Lock (sometimes called MutEx - Mutual Exclusion).
        Lock will have two functions:
        - acquire: get hold of the lock; if not available, thread will wait
        - release: release hold of the lock
        """
        print(f'thread {thread_name} starting update')
        print(f'thread {thread_name} trying to get lock')
        with self._lock:
            print(f'thread {thread_name} got the lock')

            local_copy = self.value
            local_copy += 1

            # simulate thread swap
            time.sleep(1)

            self.value = local_copy
            print(f'thread {thread_name} releases the lock')
        print(f'thread {thread_name} ending update')


fake_database = FakeDatabase()
print(f'starting db value = {fake_database.value}')

NUM_THREADS = 3

with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    executor.map(lambda x: fake_database.update(x), range(NUM_THREADS))
    executor.shutdown(wait=True)

print(f'ending db value = {fake_database.value}')
