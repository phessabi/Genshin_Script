import keyboard as kb
from pynput import keyboard
from pynput.keyboard import Controller, Key
import time

print("Genshin Efficient Running Script!")

K = Controller()

SPRINT = False
RUN = True
	

def run(arg):
	while arg[0]:
		while arg[1]:
			K.press('s')
			K.release('s')
			time.sleep(0.5)
		
	
def saj(key):
	global RUN, SPRINT
	if key == keyboard.Key.esc:		
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

t = Thread(target=run, args=[RUN, SPRINT])
t.start()

listener = keyboard.Listener(on_press=saj)
listener.start()
listener.join()
t.join()



	
