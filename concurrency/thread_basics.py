import threading
import time


def async_task():
    time.sleep(3)


def concurrent_function():
    print(f'function start on thread {threading.get_ident()}')
    async_task()
    print(f'function end   on thread {threading.get_ident()}')


print(f'main start on thread {threading.get_ident()}')
thread = threading.Thread(target=concurrent_function, daemon=True)
thread.start()
thread.join()
print(f'main end   on thread {threading.get_ident()}')