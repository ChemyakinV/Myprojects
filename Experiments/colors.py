import random
color = ''

def random_color(shade):
	return str(random.randint(10, 99))+str(random.randint(10, 99))+str(random.randint(10, 99))

def red(shade):
	return shade+'0000'

def green(shade):
	return '00'+shade+'00'

def blue(shade):
	return '0000'+shade

def white(shade):
	return shade*3
