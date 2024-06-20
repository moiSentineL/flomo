def debug_print(message: str):
    with open("debug.log", "a") as f:
        f.write(message+"\n")
