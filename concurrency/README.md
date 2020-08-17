## 2020-08-16 Concurrency
trying out contents of 
https://docs.python.org/3/library/concurrency.html
with reference to
https://realpython.com/intro-to-python-threading/

- 2020-08-16 thread_basics.py
  - create a thread with threading.Thread()
  - thread with daemon=True terminates when program exits
  - otherwise program waits for thread with daemon=False to terminate
  - thread.start() to start the thread
  - thread.join() to wait for the thread to terminate
  - RuntimeError("threads can only be started once")

- 2020-08-16 multiple_threads.py
  - manually manage threads through iteration
  - note that order of threads finishing is not guaranteed

- 2020-08-17 thread_pool.py
  - use concurrent.futures.ThreadPoolExecutor()
  - 3 executor functions - .submit(), .map(), .shutdown()
  - simple syntax to populate threads

