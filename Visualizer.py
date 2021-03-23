import tkinter as tk                                            #Нужен для визуализации пользовательского интерфейса
import random                                                   #Нужен для того чтобы каждый запуск программы давал случайный результат
import pygame 													#Нужен для отрисовки анимации
from pygame.locals import *
from OpenGL.GL import *											#Нужен для обработки математических операций для 3д объектов 
from OpenGL.GLU import *
import numpy as np 												#Нужен для работы с массивами
import librosa 													#Нужен для анализа музыкального файда

'''Количество плиток будет будет square^2 '''
square = 8

def getmusic(path):
	time_series, sample_rate = librosa.load('2.wav')
	arg1 = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))
	return arg1

edges = ((0, 1),
		( 0, 2),
		( 0, 4),
		( 3, 7),
		( 3, 1),
		( 3, 2),
		( 5, 1),
		( 5, 4),
		( 5, 7),
		( 6, 7),
		( 6, 4),
		( 6, 2))

'''Номер цвета являеться его высотой, а /255 нужно для записи в PGB формате'''
colors = ((255/255,   0/255,   0/255),#0
		(  255/255,   0/255, 205/255),#1
		(   60/255,   0/255, 255/255),#2
		(    0/255, 196/255, 255/255),#3
		(    0/255, 255/255, 154/255),#4
		(    0/255, 255/255,  17/255),#5
		(  188/255, 255/255,   0/255),#6
		(  255/255, 255/255,   0/255),#7
		(  255/255, 145/255,   0/255),#8
		(  255/255, 255/255, 255/255))#9


class cube():
	'''Функция отрисовки кубов'''
	def __init__(self, X, Z, Y, render):
		'''переменная r спарашивает: рендерить или нет?'''
		if render == 1:
			self.verticies = ((1, Y, 1),#0
						( 1, Y,-1),#1
						( 1,-1, 1),#2
						( 1,-1,-1),#3
						(-1, Y, 1),#4
						(-1, Y,-1),#5
						(-1,-1, 1),#6
						(-1,-1,-1))#7
			'''Этот блок ответственен за заскрашивание кубов'''
			#glBegin(GL_QUADS)
			#glColor3fv(colors[Y])
			#glEnd()

			'''Это отвечает за сборку кубов'''
			glBegin(GL_LINES)
			for edge in edges:
				for vertex in edge:
					glVertex3f(self.verticies[vertex][0] + X, self.verticies[vertex][1], self.verticies[vertex][2] + Z)
			glEnd()


def main(name, path):
	'''Основная исполняемая функция'''
	pygame.init()													#Запускаем модуль Pygame
	display = (600, 600)											#Задаем разрешение экрана

	win =  pygame.display.set_mode(display, DOUBLEBUF | OPENGL)		#Задаем параметры окна программы
	pygame.display.set_caption('Visualizer_3D: ' + name)			#Задаем название окна

	glMatrixMode(GL_PROJECTION)
	gluPerspective(45, (display[0] / display[1]), 0.1, 75.0)		#Задаем параметры перспективы в 45 градусов
	glMatrixMode(GL_MODELVIEW)										

	glTranslatef(-5, -5, -25)										#Задаем начальное положение игрока
	glRotatef(3, 0, -15, 0)											#Задаем начальный поворот камеры

	#Технические переменные
	speed = 2
	s = 0
	f = 2
	sample = 0
	note = 0
	frame_time = 10000												#Время жизни одного кадра анимации
	current_mv_mat = (GLfloat * 16)()								#Получение тисходной матрицы
	sum_rot_updown = 3												#Контроль наклона по вертикали
	
	amount_of_samples = len(getmusic(path))
	arg1 = getmusic(path)

	while True:

		for event in pygame.event.get():
			'''Перехват момента закрытия файла для последующего удаления кэша программы'''
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		'''Перехват всех действий пользователя'''
		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_ESCAPE]:
			pygame.quit()
			'''При нажатии Esc пользователь возвращается на исходное окно программы'''
			start_window = programm()
			start_window.mainLoop()

		'''Получаем текущую матрицу и исходную'''
		glGetFloatv(GL_MODELVIEW_MATRIX, current_mv_mat)
		glLoadIdentity()

		# Rotation Right and Left
		if pressed[pygame.K_LEFT]:
			glRotatef(speed / 2, 0, -1, 0)
			

		if pressed[pygame.K_RIGHT]:
			glRotatef(speed / 2, 0, 1, 0)
			

		# Walk with WASD
		if pressed[pygame.K_w]:
			glTranslate(0, 0, 1 / speed)
		if pressed[pygame.K_s]:
			glTranslate(0, 0, -1 / speed)
		if pressed[pygame.K_a]:
			glTranslate(1 / speed, 0, 0)
		if pressed[pygame.K_d]:
			glTranslate(-1 / speed, 0, 0)

		# Walk Up and Down With ESPACE and SHIFT
		if pressed[pygame.K_SPACE]:
			glTranslate(0, -1 / speed, 0)
		if pressed[pygame.K_LSHIFT]:
			glTranslate(0, 1 / speed, 0)

		'''Перемножение матриц для получения нового угла поворота'''
		glMultMatrixf(current_mv_mat)

		'''Поворот по вертикали'''
		if pressed[pygame.K_UP]:
			sum_rot_updown -= speed / 2
		if pressed[pygame.K_DOWN]:
			sum_rot_updown += speed / 2

		'''Обновление текущей матрицы'''		
		glPushMatrix()
		glGetFloatv(GL_MODELVIEW_MATRIX, current_mv_mat)
		glLoadIdentity()
		glRotatef(sum_rot_updown, 1, 0, 0)
		glMultMatrixf(current_mv_mat)

		'''Основной блок отрисовки'''
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		
		'''Когда проходит время N положение кубов меняеться'''
		if pygame.time.get_ticks() <= f*frame_time:

			'''Этот блок отвечает за постройку и расположение кубов'''
			for x in range(square):
				for z in range(square):
					try:
						cube(X = x * 2.5, Z = z * 2.5, Y = round(arg1[sample][note], 2), render = 1)
						print(arg1[sample][note])
						note += 1
					except IndexError:
						quit()
		
		else:
			print(amount_of_samples)
			amount_of_samples -= 1	#Уменьшение количества 16 символьных стэков для ограничения времени жизни цикла
			f += 1					#Увеличения параметра жизния оного кадра анимации для его смены на новый кадр
			sample += 1				#Увеличиваем номер сэмпла
			note = 0				#Берем следующую ноту

			if amount_of_samples == 0:
				'''В случае окончания музыки остановить отрисовку'''
				pygame.quit()
				quit()

		glPopMatrix()				#Стираем матрицу для перерисовки
		pygame.display.flip()		#Смена кадров для плавной отрисовки
		pygame.time.delay(25)		#Время жизни одного Frame


class programm():
	'''Этот класс нужен для много кратного вызова статового окна'''
	def __init__(self):
		'''Задаем параметры стартового окна'''
		self.root = tk.Tk()
		self.root.resizable(width=False, height=False)
		self.root.title('Visualizer_3D')
		self.root['bg'] = 'purple'
		#self.root.iconbitmap('bin/Visualizer.ico')
		self.root.resizable(width = None, height = None)
		self.start()

	def start(self):
		'''Стартовое окно программы'''
		'''Это временные переменные для принятия входных данных пользователя'''
		self.path = tk.StringVar()
		self.name = tk.StringVar()
		
		'''Здесь я определяю элементы на статовой странице'''
		self.Label_name = tk.Label(self.root, text = 'Имя проекта        ', bg = 'purple', fg = 'white')
		self.add_music = tk.Label(self.root, text =  'Путь к файлу mp3   ', bg = 'purple', fg = 'white')
		
		self.project_name = tk.Entry(self.root, width = 40, textvariable = self.name)
		self.user_input = tk.Entry(self.root, width = 40, textvariable = self.path)

		self.render_btn = tk.Button(self.root, width = 50, text = 'Пуск', bg = 'orange', fg = 'white', command = lambda: self.launch(self.name.get(), self.path.get()))

		'''А здесь определяю их местоположение относительно друг друга и другие параметры элементов'''
		self.Label_name.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.W)
		self.project_name.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tk.W)
		self.add_music.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tk.W)
		self.user_input.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = tk.W)
		self.render_btn.grid(row = 2, column = 0, padx = 10, pady = 10, columnspan = 3)

	def launch(self, name, path):
		'''Уничтожаем окно запуска и создаем папку для рендеринга кадров'''
		self.root.destroy()
		#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
		'''Переход к программе рендера'''
		main(name, path)
		#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
	
	def mainLoop(self):
		'''Данная функция нужна для корректной работы и отображения модуля tkinter'''
		self.root.mainloop()



'''Это переменная нужна для многократного запуска программы, 
   хотя можно было обойтись без ООП, а например через функции,
   но ООП выглядит более аккуратно и структурировано'''
app = programm()

'''Вызов этой функции нужен для запуска цикла отрисовки виджетов Tkinter'''
app.mainLoop()
