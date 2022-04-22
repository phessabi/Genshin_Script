import time
from threading import Thread

from pynput import keyboard
from pynput.keyboard import Controller
from pynput.mouse import Controller as Controller_Mouse
from pynput.mouse import Button


mouse = Controller_Mouse()

print("Genshin Efficient Running Script!")

K = Controller()

CLICK = False
RUN = True


def run():
	while RUN:
		if CLICK:
			mouse.press(Button.left)
			mouse.release(Button.left)
			time.sleep(0.5)
			K.press(keyboard.Key.esc)
			K.release(keyboard.Key.esc)


def run_control_callback(key):
	global RUN, CLICK
	if key == keyboard.Key.ctrl_r:
		RUN = False
		return False
	try:
		k = key.char
	except AttributeError:
		k = key.name

	if k == '[':
		print('start')
		CLICK = True

	if k == ']':
		print('end')
		CLICK = False


t = Thread(target=run)
t.start()

listener = keyboard.Listener(on_press=run_control_callback)
listener.start()
print('Ready!')
listener.join()
t.join()
