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
  
- 2020-08-17 deadlock_1.py deadlock_2.py
  - deadlock_1.py: deadlock where two different threads block one another
  - deadlock_2.py: deadlock where a thread depends on a new thread to be populated,
    but no new thread is created due to thread pool size

- 2020-10-03 race_condition.py
  - create a mock database where 'value' is shared across threads
  - 'value' is incremented by multiple threads simultaneously
  - notice how each thread override the changes from other threads
