import time


class Flow:
    def __init__(self) -> None:
        self.global_start_time = 0

        # Current Session
        self.start_time = 0
        self.time_elapsed = 0
        self.time_for_break = 0

    def initialize_flow(self) -> None:
        self.global_start_time = time.time()
        self.start_time = self.global_start_time

    def break_flow(self) -> None:
        self.time_elapsed = round(time.time() - self.start_time, 2)
        self.time_for_break = round(self.time_elapsed/5, 2)
        self.start_time = 0

    def restart_flow(self) -> None:
        self.start_time = time.time()
        self.time_elapsed = 0
        self.time_for_break = 0
