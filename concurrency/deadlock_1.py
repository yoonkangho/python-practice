import threading
import time
from concurrent.futures import ThreadPoolExecutor


def wait_on_b():
    print(f'thread {threading.get_ident()} start')
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    print(f'thread {threading.get_ident()} end')
    return 5


def wait_on_a():
    print(f'thread {threading.get_ident()} start')
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    print(f'thread {threading.get_ident()} end')
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)