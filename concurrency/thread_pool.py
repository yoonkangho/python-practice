import threading
import time
from concurrent.futures import ThreadPoolExecutor


def async_task():
    time.sleep(3)


def concurrent_function(index):
    print(f'function start on thread {index}')
    async_task()
    print(f'function end   on thread {index}')


print(f'main start on thread {threading.get_ident()}')

threads = []
NUM_THREADS = 3

with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:

    executor.map(concurrent_function, range(NUM_THREADS))
    # or alternatively, use executor.submit() to create threads one at a time

    print('main waiting for shutdown')
    executor.shutdown(wait=True)
    print('main shutdown complete')

    # or alternatively, make use of the generator returned from executor.map()
    # futures = executor.map(concurrent_function, range(NUM_THREADS))

print(f'main end   on thread {threading.get_ident()}')
