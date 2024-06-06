import time


class Flow:
    def __init__(self) -> None:
        self.start_time = 0
        self.time_elapsed = 0
        self.time_for_break = 0

    def initialize_flow(self):
        self.start_time = time.time()

    def restart_flow(self):
        pass

    def break_flow(self):
        self.time_elapsed = round(time.time() - self.start_time, 2)
        self.time_for_break = round(self.time_elapsed/5, 2)
