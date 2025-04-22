import time
from timing_collector import TimingCollector

def timed(event_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            collector = TimingCollector()
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            collector.record_event(event_name, start, end)
            return result
        return wrapper
    return decorator

# Sample functions
@timed('function_a')
def function_a():
    time.sleep(0.1)
    function_b()
    function_c()

@timed('function_b')
def function_b():
    time.sleep(0.05)
    function_d()

@timed('function_c')
def function_c():
    time.sleep(0.02)

@timed('function_d')
def function_d():
    time.sleep(0.03)

if __name__ == '__main__':
    function_a()
    TimingCollector().print_events()
