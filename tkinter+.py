import tkinter as tk

root = tk.Tk()
c1 = tk.Canvas(root, width = 500, height = 500, bg = 'black', highlightthickness = 0)
c1.pack()

class Button():
	def __init__(self, x, y, w, h, r, color, text, font, txt_color, tag):
		self.x, self.y, self.w, self.h = x, y, w, h
		d = r*2
		c1.create_arc(x, y, x+d, y+d, extent = 90, fill = color, start = 90,  outline = color, tags = tag)
		c1.create_arc(x+w-d, y, x+w, y+d, extent = 90, fill = color, start = 0,   outline = color, tags = tag)
		c1.create_arc(x, y+h-d, x+d, y+h, extent = 90, fill = color, start = 180, outline = color, tags = tag)
		c1.create_arc(x+w-d, y+h-d, x+w, y+h, extent = 90, fill = color, start = 270, outline = color, tags = tag)
		c1.create_rectangle(x+r, y, x+w-r+1, y+h, outline = color, fill = color, tags = tag)
		c1.create_rectangle(x, y+r, x+w, y+h-r, outline = color, fill = color, tags = tag)
		c1.create_text(x+w//2, y+h//2, text = text, fill = txt_color, font = font, tags = str(tag)+'_text')
		c1.bind('<Button-1>', self.pressed)
	def pressed(self, event):
		if event.x >= self.x and event.x <= self.x+self.w and event.y >= self.y and event.y <= self.y+self.h:
			c1.itemconfig('button', fill = 'red', outline = 'red')

a = Button(100, 100, 100, 30, 15, 'Blue', 'Push me!', ('Helvetica 10 '), 'white', 'button')



root.mainloop()