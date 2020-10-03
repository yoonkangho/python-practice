# standard imports
from concurrent.futures import ThreadPoolExecutor
import time

# 3rd party imports

# application imports


class FakeDatabase():

    def __init__(self):
        self.value = 0

    def update(self, thread_name):
        print(f'thread {thread_name} starting update')

        local_copy = self.value
        local_copy += 1

        # simulate thread swap
        time.sleep(1)

        self.value = local_copy

        print(f'thread {thread_name} ending update')


fake_database = FakeDatabase()
print(f'starting db value = {fake_database.value}')

NUM_THREADS = 3

with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    executor.map(lambda x: fake_database.update(x), range(NUM_THREADS))
    executor.shutdown(wait=True)

print(f'ending db value = {fake_database.value}')
