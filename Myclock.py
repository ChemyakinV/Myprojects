import tkinter as tk
import math 
import time
import random 

root = tk.Tk()
root.title('Myclock')
root.resizable(False, False)
root.attributes('-toolwindow', True)

c1 = tk.Canvas(root, width = 500, height = 500, bg = 'black', highlightcolor = 'black', highlightthickness = 0)
c1.focus_set()
c1.pack()

lines = []
amount_of_lines = 50
x = 250
y = 250
zeroy = 200
state = 0
bw = 'white'

colors = ['f00', 'f08', 'ff00e5', 'c0f', '9d00ff', '0008ff', '0095ff', '0ff', '00ffb3', '0f5', '2f0', 'aeff00', 'fbff00', 'ffc800', 'fa0', 'ff6a00']
	
def start():
	for i in range(0, 360, 6):
		c1.create_line(100*math.cos(math.radians(i-90))+250, 100*math.sin(math.radians(i-90))+zeroy, 110*math.cos(math.radians(i-90))+250, 110*math.sin(math.radians(i-90))+zeroy, width = 2, fill = 'white')
		if i%30 == 0:
			c1.create_line(95*math.cos(math.radians(i-90))+250, 95*math.sin(math.radians(i-90))+zeroy, 120*math.cos(math.radians(i-90))+250, 120*math.sin(math.radians(i-90))+zeroy, width = 2, fill = 'white')
			c1.create_text(140*math.cos(math.radians(i-90))+250, 140*math.sin(math.radians(i-90))+zeroy, text = str(int(i/30)), tags = i/30, font = ('Brush Script MT', 15, 'italic bold'), fill = '#'+colors[random.randint(0, len(colors)-1)])
		root.update()
		c1.delete(0.0)
		time.sleep(0.01)
	
	c1.create_text(140*math.cos(math.radians(-90))+250, 140*math.sin(math.radians(-90))+zeroy, text = '12', tags = 12.0, font = ('Brush Script MT', 20, 'italic bold'), fill = '#'+colors[random.randint(0, len(colors)-1)])
	root.update()

	clock_hands()

def clock_hands():
	global state, bw
	hour = time.localtime().tm_hour%12
	minute = time.localtime().tm_min
	second = time.localtime().tm_sec

	c1.create_line(250, zeroy, 90*math.cos(math.radians(second*6-90))+250, 90*math.sin(math.radians(second*6-90))+zeroy, tags = 'SEC', fill = 'white', width = 1)
	c1.create_line(250, zeroy, 80*math.cos(math.radians(minute*6-90))+250, 80*math.sin(math.radians(minute*6-90))+zeroy, tags = 'MIN', fill = 'red', width = 2)
	c1.create_line(250, zeroy, 70*math.cos(math.radians(hour%12*30-90))+250, 70*math.sin(math.radians(hour%12*30-90))+zeroy, tags = 'HOUR', fill = 'blue', width = 3)
	root.update()

	while True:
		if time.localtime().tm_sec != second:
			try:
				c1.delete('SEC')
				c1.delete('TIME')
			except:
				return 0
			second = time.localtime().tm_sec
			c1.create_line(250, zeroy, 90*math.cos(math.radians(second*6-90))+250, 90*math.sin(math.radians(second*6-90))+zeroy, tags = 'SEC', fill = 'white', width = 1)
			lines(second)
			c1.create_text(250, 400, text = time.asctime(), font = ('Ink Free', 20, ), fill = 'white', tags = 'TIME')
			root.update()
			if second == 0:
				for i in range(1,13):
					c1.delete(float(i))
				for i in range(0, 360, 6):
					if i%30 == 0:
						c1.create_text(140*math.cos(math.radians(i-90))+250, 140*math.sin(math.radians(i-90))+zeroy, text = str(int(i/30)), tags = i/30, font = ('Brush Script MT', 15, 'italic bold'), fill = '#'+colors[random.randint(0, len(colors)-1)])
					root.update()
				c1.delete(0.0)
				c1.create_text(140*math.cos(math.radians(-90))+250, 140*math.sin(math.radians(-90))+zeroy, text = '12', tags = 12.0, font = ('Brush Script MT', 20, 'italic bold'), fill = '#'+colors[random.randint(0, len(colors)-1)])
				root.update()

				if state == 0:
					state = 1
					bw = 'black'
				else:
					state = 0
					bw = 'white'

		if time.localtime().tm_min != minute:
			try:
				c1.delete('MIN')
			except:
				return 0
			minute = time.localtime().tm_min
			c1.create_line(250, zeroy, 80*math.cos(math.radians(minute*6-90))+250, 80*math.sin(math.radians(minute*6-90))+zeroy, tags = 'MIN', fill = 'red', width = 2)
			root.update()

		if time.localtime().tm_hour != hour:
			try:
				c1.delete('HOUR')
			except:
				return 0
			hour = time.localtime().tm_hour%12
			c1.create_line(250, zeroy, 70*math.cos(math.radians(hour*30-90))+250, 70*math.sin(math.radians(hour*30-90))+zeroy, tags = 'HOUR', fill = 'blue', width = 3)
			root.update()

def lines(second):
	if bw =='white':
		c1.create_line(100*math.cos(math.radians(second*6-90))+250, 100*math.sin(math.radians(second*6-90))+zeroy, 110*math.cos(math.radians(second*6-90))+250, 110*math.sin(math.radians(second*6-90))+zeroy, width = 2, fill = bw)
		if second%5 == 0:
			c1.create_line(95*math.cos(math.radians(second*6-90))+250, 95*math.sin(math.radians(second*6-90))+zeroy, 120*math.cos(math.radians(second*6-90))+250, 120*math.sin(math.radians(second*6-90))+zeroy, width = 2, fill = bw)
	else:
		c1.create_line(95*math.cos(math.radians(-90))+250, 95*math.sin(math.radians(-90))+zeroy, 120*math.cos(math.radians(-90))+250, 120*math.sin(math.radians(-90))+zeroy, width = 2, fill = 'white')
		c1.create_line(95*math.cos(math.radians((second-1)*6-90))+250, 95*math.sin(math.radians((second-1)*6-90))+zeroy, 120*math.cos(math.radians((second-1)*6-90))+250, 120*math.sin(math.radians((second-1)*6-90))+zeroy, width = 4, fill = bw)

start()

root.mainloop()
