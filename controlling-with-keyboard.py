#!/usr/bin/python3
import time, serial
from pynput.keyboard import Key, Listener

def on_press(key):
	key = str(key)
	if key == "'w'":
		print('{0} pressed'.format(key))
		s.write(b's')
	elif key == "'s'":
		print('{0} pressed'.format(key))
		s.write(b'w')

def on_release(key):
	key = str(key)
	if key == "'q'":
		return False
	elif key == "'w'":
		print('{0} release'.format(key))
		s.write(b's')
	elif key == "'s'":
		print('{0} pressed'.format(key))
		s.write(b'w')

# Collect events until released

# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as s:
	time.sleep(1)
	with Listener(on_press=on_press, on_release=on_release) as listener:
	    listener.join()