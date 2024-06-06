#! /bin/env python3
import time

start_time = time.time()
print("Started flow!")

while True:
    input()
    time_elapsed = round(time.time() - start_time, 2)
    print("Time elapsed: ", time_elapsed)

    time_for_break = round(time_elapsed/5, 2)
    print("Time for break: ", time_for_break)

    break


#testing pr 