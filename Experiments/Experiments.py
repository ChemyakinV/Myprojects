import tkinter as tk 					#Нужен для визуального оформления программы
import ctypes							#Нужен для получения размеров монитора
import random							
import math		
import colors 				

inf 	    	= ctypes.windll.user32			#Получаем все сведенья о системе
width  	    	= inf.GetSystemMetrics(0)		#Получаем ширину экрана
height 	    	= inf.GetSystemMetrics(1)		#Получаем высоту экрана
particles   	= []							#Массив для хранения всех чатиц, т.е. объектов класса Particle
mode        	= 'b'							#Это тип цветовой палитры, понажимайте на клавиатуре 'r', 'g', 'b', 'w', 'o', последнее рекомендуется нажать пару раз
default_clr     = '999999'
cnf         	= {								#Список параметров
	'bgcolor'		  : 'black',    			#Цвет фона
	'particlecolor'   : '000099',				#Цвет частицы
	'particleradiuse' : 3,						#Радиус частицы
	'particlecount'   : 45,						#Количество частиц
	'particlespeed'   : 10,						#Максимальная скорость частицы
	'linelenght'      : 200,					#Радиус, в пределах которого строится соединени данной точки с другой 
	'brightness'      : 10,						#Это параметр отвечает за яркость линий соединений, чем выше, тем бледнее линии соединений
}

def default(length):
	cnf.update({'particlecolor' : default_clr})
	return default_clr

color =  {	'o' : '809070',
			'r' : '990000',
			'g' : '009900',
			'b' : '000099',
			'w' : '999999', 
			'd' : default_clr}

color_modes = {
	'o' : colors.random_color,
	'r' : colors.red,
	'g' : colors.green,
	'b' : colors.blue,
	'w' : colors.white,
	'd' : default}

root = tk.Tk()									
root.attributes('-fullscreen', True)			#При запуске програмы сразу открываем окно на полный экран

c1 = tk.Canvas(root, width = 100, height = 1000, bg = cnf['bgcolor'], highlightthickness = 0, cursor= 'None') 	#Создаем Canvas, размеры потом поменяются
c1.focus_set()							#Делаем наше окно активным
c1.pack(fill = 'both', expand = 1)		#Растягиваем Canvas на весь экран

class Particle():
	'''Класс создания частиц, и редактирования их свойств'''
	def __init__(self):
		'''Задаем произвольную позицию'''
		self.x = width//2 #random.randint(cnf['particleradiuse'], width - cnf['particleradiuse']) 
		self.y = height//2 #random.randint(cnf['particleradiuse'], height - cnf['particleradiuse'])
		'''Задаем произвольную скорость в +- диапозоне от максимальной'''
		self.xspeed = round(random.random()*cnf['particlespeed']*2-cnf['particlespeed'])
		self.yspeed = round(random.random()*cnf['particlespeed']*2-cnf['particlespeed'])

	def position(self):
		'''Изменяем позицию частицы, учитывая собственную скорость и столкновение с краем экрана'''
		if self.x+self.xspeed+cnf['particleradiuse'] >= width or self.x+self.xspeed-cnf['particleradiuse'] <= 0:
			self.xspeed *= -1		#При привышении границ экрана менять горизонтальную скорость на противоположную
		if self.y+self.yspeed+cnf['particleradiuse'] >= height or self.y+self.yspeed-cnf['particleradiuse'] <= 0:
			self.yspeed *= -1		#При привышении границ экрана менять вертикальную скорость на противоположную
		'''Меняем координаты прибавив скорость'''
		self.x += self.xspeed
		self.y += self.yspeed

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def redraw(self):	
		'''Функция отрисовки частицы'''
		self.circle = c1.create_oval(self.x-cnf['particleradiuse'], self.y-cnf['particleradiuse'], self.x+cnf['particleradiuse'], self.y+cnf['particleradiuse'], fill = '#'+cnf['particlecolor'], width = 1)
		
def redrawParticles():
	'''Основная функция'''
	while True:
		try:
			'''Перехватываем нажатия с клавиатуры для изменения цветовой палитры или завершения программы'''
			c1.bind("<Key>", lambda event: change_mode(event.keysym))
			c1.bind("<Escape>", lambda event: root.destroy())	#Завершение программы
		except:
			'''Если root.destroy то программа завершается'''
			break
		try:
			'''Отчицаем Canvas для следующего кадра'''
			c1.delete('all')
		except:
			pass
		for i in range(cnf['particlecount']):
			'''Для каждой частицы рассчитываем новое положение и отрисовываем частицу там'''
			particles[i].position()
			particles[i].redraw()
		lines()			#Рисуем соединения между частиц
		root.update()	#Обновляем root для отображения результата


def change_mode(new_mode):
	global mode
	
	if new_mode == 'd':
		global default_clr
		default_clr = str(random.randint(10,99))+str(random.randint(10,99))+str(random.randint(10,99))
	try:
		cnf.update({'particlecolor': color[new_mode]})
		mode = new_mode
	except:
		pass

def shade(length):
	'''Яркость линии зависит от расстояния, чем ближе тем ярче'''	
	'''Если значение цвета зависит только от одного показателя RGB или является монохромным то выполняем рассчет яркости линии соединениея'''			
	shade = cnf['linelenght'] - length - cnf['brightness']
	if shade >= 100:
		shade = 99
	if shade <= 0:
		shade = 0
	if shade < 10:
		shade = '0'+str(shade)
	
	shade = str(shade)
	return '#'+color_modes[mode](shade) 


def lines():
	'''Проверяем дистанцию до каждой из точек'''
	for i in range(0, len(particles)):
		ip = particles[i]
		for j in range(i+1, len(particles)):
			jp = particles[j]
			x1 = ip.get_x()		#Координаты первой точки
			y1 = ip.get_y()
			x2 = jp.get_x()		#Координаты второй точки
			y2 = jp.get_y()
			length = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)		#Нахом расстояние между двумя точками
			if length < cnf['linelenght']**2:		#Если расстояние меньше максимальной длянны линиии, то строим соединение
				'''Рисуем линию соединения, а цвет возьмем из функции для этого'''
				length = int(math.sqrt(length))
				c1.create_line(x1, y1, x2, y2, width = 2, fill = shade(length))
				

def start():
	for i in range(cnf['particlecount']):
		'''Наполняем массив частицами с произвольными скорость, положением, направлением'''
		particles.append(Particle())
	redrawParticles()		#Вызываем функцию отрисовки

start()			#Вызываем функцию для запуска программы

root.mainloop()
