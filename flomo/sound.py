from playsound import playsound
import os

def play():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = "/beep.mp3"
    path = os.path.join(dir_path + file)

    # os.system("mpg123 -q " + path)
    # print(path)

if __name__ == "__main__":
    play()