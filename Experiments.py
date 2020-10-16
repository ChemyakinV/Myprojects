import tkinter as tk 					#Нужен для визуального оформления программы
import ctypes							#Нужен для получения размеров монитора
import random							
import math								

inf 	    	= ctypes.windll.user32			#Получаем все сведенья о системе
width  	    	= inf.GetSystemMetrics(0)		#Получаем ширину экрана
height 	    	= inf.GetSystemMetrics(1)		#Получаем высоту экрана
particles   	= []							#Массив для хранения всех чатиц, т.е. объектов класса Particle
mode        	= 'b'							#Это тип цветовой палитры, понажимайте на клавиатуре 'r', 'g', 'b', 'w', 'o', 'd', последнее рекомендуется нажать пару раз
colors      	= '' 							#Этот параметр нужен для работы цветовой палитры  mode == 'd'
cnf         	= {								#Список параметров
	'bgcolor'		  : 'black',    			#Цвет фона
	'particlecolor'   : 'blue',					#Цвет частицы
	'particleradiuse' : 3,						#Радиус частицы
	'particalcount'   : 40,						#Количество частиц
	'particalspeed'   : 5,						#Максимальная скорость частицы
	'linelenght'      : 200,					#Радиус, в пределах которого строится соединени данной точки с другой 
	'brightness'      : 90						#Это параметр отвечает за яркость линий соединений, чем выше, тем бледнее линии соединений
}

root = tk.Tk()									
root.attributes('-fullscreen', True)			#При запуске програмы сразу открываем окно на полный экран

c1 = tk.Canvas(root, width = 100, height = 1000, bg = cnf['bgcolor'], highlightthickness = 0, cursor= 'None') 	#Создаем Canvas, размеры потом поменяются
c1.focus_set()							#Делаем наше окно активным
c1.pack(fill = 'both', expand = 1)		#Растягиваем Canvas на весь экран

class Particle():
	'''Класс создания частиц, и редактирования их свойств'''
	def __init__(self):
		'''Задаем произвольную позицию'''
		self.x = random.randint(cnf['particleradiuse'], width - cnf['particleradiuse']) 
		self.y = random.randint(cnf['particleradiuse'], height - cnf['particleradiuse'])
		'''Задаем произвольную скорость в +- диапозоне от максимальной'''
		self.xspeed = random.random()*cnf['particalspeed']*2-cnf['particalspeed']
		self.yspeed = random.random()*cnf['particalspeed']*2-cnf['particalspeed']

	def position(self):
		'''Изменяем позицию частицы, учитывая собственную скорость и столкновение с краем экрана'''
		if self.x+self.xspeed+cnf['particleradiuse'] >= width or self.x+self.xspeed-cnf['particleradiuse'] <= 0:
			self.xspeed *= -1		#При привышении границ экрана менять горизонтальную скорость на противоположную
		if self.y+self.yspeed+cnf['particleradiuse'] >= height or self.y+self.yspeed-cnf['particleradiuse'] <= 0:
			self.yspeed *= -1		#При привышении границ экрана менять вертикальную скорость на противоположную
		'''Меняем координаты прибавив скорость'''
		self.x += self.xspeed
		self.y += self.yspeed

	def coords(self, axis):
		'''Метод возвращает координаты точки'''
		if axis == 'x':
			return self.x
		else:
			return self.y

	def redraw(self):	
		'''Функция отрисовки частицы'''
		try:
			self.circle = c1.create_oval(self.x-cnf['particleradiuse'], self.y-cnf['particleradiuse'], self.x+cnf['particleradiuse'], self.y+cnf['particleradiuse'], fill = cnf['particlecolor'], width = 1)
		except:
			pass

def redrawParticles():
	'''Основная функция'''
	while True:
		try:
			'''Перехватываем нажатия с клавиатуры для изменения цветовой палитры или завершения программы'''
			c1.bind("<r>", lambda event: changemode('r'))		#красная тема
			c1.bind("<g>", lambda event: changemode('g'))		#зеленая
			c1.bind("<b>", lambda event: changemode('b'))		#синяя
			c1.bind("<w>", lambda event: changemode('w'))		#серая
			c1.bind("<d>", lambda event: changemode('d'))		#все линии одного случайного цета
			c1.bind("<o>", lambda event: changemode('o'))		#каждая линия случайного цвета
			c1.bind("<Escape>", lambda event: root.destroy())	#Завершение программы
		except:
			'''Если root.destroy то программа завершается'''
			break
		try:
			'''Отчицаем Canvas для следующего кадра'''
			c1.delete('all')
		except:
			pass
		for i in range(cnf['particalcount']):
			'''Для каждой частицы рассчитываем новое положение и отрисовываем частицу там'''
			particles[i].position()
			particles[i].redraw()
		lines()			#Рисуем соединения между частиц
		root.update()	#Обновляем root для отображения результата

def changemode(new_mode):
	global mode, colors
	'''Меняем цвет для режима d'''
	colors = '#'+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9)) 
	mode   = new_mode	#Изменяем текущую цветовую тему на новую

def color(length):
	'''Яркость линии зависит от расстояния, чем ближе тем ярче'''
	if mode == 'r' or mode == 'g' or mode == 'b' or mode == 'w':	
		'''Если значение цвета зависит только от одного показателя RGB или является монохромным то выполняем рассчет яреости линии соединениея'''			
		color = cnf['linelenght']-int(round(length/cnf['linelenght'], 2)*100)-cnf['brightness']
		if color >= 100:
			color = 99
		if color <= 0:
			color = 0
		if color < 10:
			color = '0'+str(color)
		else:
			color = str(color)

		if mode == 'r':
			cnf.update({'particlecolor': 'red'})
			return '#'+color+'0000'
		elif mode == 'g':
			cnf.update({'particlecolor': 'green'})
			return '#'+'00'+color+'00'
		elif mode == 'b':
			cnf.update({'particlecolor': 'blue'})
			return '#'+'0000'+color
		elif mode == 'w':
			cnf.update({'particlecolor': 'grey'})
			return '#'+color+color+color

	elif mode == 'o':
		#Случайный цвет каждой линии по отдельности
		cnf.update({'particlecolor': 'purple'})
		return '#'+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
	else:
		#Случайный цвет для всех линий одинаковый
		cnf.update({'particlecolor': 'purple'})
		return colors

def lines():
	'''Проверяем дистанцию до каждой из точек'''
	for i in particles:
		for j in particles:
			x1 = i.coords('x')		#Координаты первой точки
			y1 = i.coords('y')
			x2 = j.coords('x')		#Координаты второй точки
			y2 = j.coords('y')
			length = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1), 2))		#Нахом расстояние между двумя точками
			if length < cnf['linelenght']:										#Если расстояние меньше максимальной длянны линиии, то строим соединение
				try:
					'''Рисуем линию соединения, а цвет возьмем из функции для этого'''
					c1.create_line(x1, y1, x2, y2, width = 2, fill = color(length))
				except:
					pass

def start():
	for i in range(cnf['particalcount']):
		'''Наполняем массив частицами с произвольными скорость, положением, направлением'''
		particles.append(Particle())
	redrawParticles()		#Вызываем функцию отрисовки

start()			#Вызываем функцию для запуска программы

root.mainloop()
