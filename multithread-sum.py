import time
from threading import Thread, Event, Lock

def sum(funcs, on_sum_changed):
    sum_tracker = [0] # make it a list so each thread can mutate it
    threads = []
    thread_lock = Lock()
    for func in funcs:
        def threaded_func():
            addition = func()
            with thread_lock:
                sum_tracker[0] += addition
                on_sum_changed(sum_tracker[0])
        threads.append(Thread(target=threaded_func))
        threads[-1].start()
    for thread in threads:
        thread.join()
    return sum_tracker[0]

    
if __name__ == "__main__":
    def expensive_function():
        time.sleep(1)
        return 100
    def cheap_function():
        time.sleep(0.1)
        return 10
    on_sum_changed = lambda sum : print("Current result: " + str(sum))
        
    result = sum([expensive_function, cheap_function], on_sum_changed)
    print("Final result: " + str(result))
