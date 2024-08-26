import time

def echo(message):
    start_time = time.perf_counter()
    print(message)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    from time import sleep, perf_counter_ns
    timePoint1 = perf_counter_ns()
    sleep(20)
    timePoint2 = perf_counter_ns()
    durationInMS = (timePoint2 - timePoint1) / 1_000_000
    print(f"Duration: {durationInMS} ms")

# Example usage
echo("Hello, world!")



