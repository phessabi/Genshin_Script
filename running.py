import time
from threading import Thread

from pynput import keyboard
from pynput.keyboard import Controller

print("Genshin Efficient Running Script!")

K = Controller()

SPRINT = False
RUN = True


def run():
    while RUN:
        if SPRINT:
            K.press(keyboard.Key.shift_l)
            time.sleep(0.1)
            K.release(keyboard.Key.shift_l)
            time.sleep(0.8)


def run_control_callback(key):
    global RUN, SPRINT
    if key == keyboard.Key.ctrl_r:
        RUN = False
        return False
    try:
        k = key.char
    except AttributeError:
        k = key.name

    if k == '[':
        print('start')
        SPRINT = True

    if k == ']':
        print('end')
        SPRINT = False


t = Thread(target=run)
t.start()

listener = keyboard.Listener(on_press=run_control_callback)
listener.start()
print('Ready!')
listener.join()
t.join()
