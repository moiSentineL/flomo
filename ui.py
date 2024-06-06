from logic import Flow

flow = Flow()
flow.initialize_flow()
print("Started flow!")

print("Waiting for input..")
input()

flow.break_flow()
print("Time elapsed: ", flow.time_elapsed, "s")
print("Time for break: ", flow.time_for_break, "s")

# Wait for flow.time_for_break
flow.restart_flow()
print("Restarted Flow!")

# repeat cycle until stop_flow
