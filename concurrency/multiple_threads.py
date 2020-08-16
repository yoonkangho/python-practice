import threading
import time


def async_task():
    time.sleep(3)


def concurrent_function(index):
    print(f'function start on thread {index}')
    async_task()
    print(f'function end   on thread {index}')


print(f'main start on thread {threading.get_ident()}')

threads = []
NUM_THREADS = 3

for index in range(NUM_THREADS):
    thread = threading.Thread(target=concurrent_function, daemon=True, args=(index, ))
    threads.append(thread)
    thread.start()

for index, thread in enumerate(threads):
    print(f'before joining thread {index}')
    thread.join()
    print(f'after  joining thread {index}')

print(f'main end   on thread {threading.get_ident()}')