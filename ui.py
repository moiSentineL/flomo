from logic import Flow

flow = Flow()
flow.initialize_flow()

print("Waiting for input..")
input()

flow.break_flow()
# Wait for flow.time_for_break
flow.start_flow()

# repeat cycle until stop_flow
