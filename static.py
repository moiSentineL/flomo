import shutil
import os
import sys
import platform

def print_empty_square(size):
    terminal_width = shutil.get_terminal_size().columns
    left_padding = (terminal_width - (size * 2 + 2)) // 2
    print("______________________________")
    for _ in range(size):
        print(" " * left_padding + "|" + " " * (size * 2) + "|")
    print(" " * left_padding + "|" + "_" * (size * 2) + "|")

size = 15

if platform.system() == "Linux":
    os.system("clear")
elif platform.system() == "Darwin":
    os.system("clear")
elif platform.system() == "Windows":
    os.system("cls")

print_empty_square(size)

# time = 10
# print("Name:")
# print("Tag:",time) 
# print("Stopwach:")
# print("kdfdjkf:")