#!python3
#traffic light using itertools and random modules

from time import sleep
import itertools
import random

colours = 'Red Green Amber'.split()
rotation = itertools.cycle(colours)

def rg_timer():
	return random.randint(5,9)

def light_rotation(rotation):
	for colour in rotation:
		if colour == 'Amber':
			print('Caution! The light is %s.\n' % colour)
			sleep(5)
		elif colour == 'Red':
			print('Stop! The light is %s.\n' % colour)
			sleep(rg_timer())
		else:
			print('Go! The light is %s.\n' % colour)
			sleep(rg_timer())


if __name__ == '__main__':
	light_rotation(rotation)
