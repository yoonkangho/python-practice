import threading
from concurrent.futures import ThreadPoolExecutor


def wait_on_future():
    print(f'thread {threading.get_ident()} start')
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())
    print(f'thread {threading.get_ident()} end')


executor = ThreadPoolExecutor(max_workers=1)
executor.submit(wait_on_future)