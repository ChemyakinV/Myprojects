import tkinter as tk
import math
import ctypes
import random

inf    = ctypes.windll.user32
width  = inf.GetSystemMetrics(0)
height = inf.GetSystemMetrics(1)

root = tk.Tk()
root.title('Serpinskiy triangle')
root['bg'] = 'black'
root.attributes('-fullscreen', True)

c1 = tk.Canvas(root, width = width-200, height = height, bg = 'black', highlightcolor = 'grey', highlightthickness = 0)
c1.grid(column = 0, row = 0)
c2 = tk.Canvas(root, width = 200 - 2, height = height, bg = 'black', highlightcolor = 'grey', highlightthickness = 1)
c2.grid(column = 1, row = 0)


root.mainloop()