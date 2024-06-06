import time


class Flow:
    def __init__(self) -> None:
        self.start_time = 0
        self.time_elapsed = 0
        self.time_for_break = 0

    def start_flow(self):
        self.start_time = time.time()
        print("Started flow!")

    def break_flow(self):
        time_elapsed = round(time.time() - self.start_time, 2)
        print("Time elapsed: ", time_elapsed, "s")

        time_for_break = round(time_elapsed/5, 2)
        print("Time for break: ", time_for_break, "s")
