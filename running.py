import keyboard as kb
from pynput import keyboard
from pynput.keyboard import Controller
import time

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

def saj(key):
    global RUN, SPRINT
    if key == keyboard.Key.shift_r:
        RUN = False
        return False
    try:
        k = key.char
    except:
        k = key.name

    if k == '[':
        print('start')
        SPRINT = True

    if k == ']':
        print('end')
        SPRINT = False


from threading import Thread

t = Thread(target=run)
t.start()

listener = keyboard.Listener(on_press=saj)
listener.start()
print('Ready!')
listener.join()
t.join()

