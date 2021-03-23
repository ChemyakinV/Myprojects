import random                                                   #Нужен для того чтобы каждый запуск программы давал случайный результат
import pygame 													#Нужен для отрисовки анимации
from pygame.locals import *
from OpenGL.GL import *											#Нужен для обработки математических операций для 3д объектов 
from OpenGL.GLU import *

def main():
	'''Основная исполняемая функция'''
	pygame.init()													#Запускаем модуль Pygame
	display = (600, 600)											#Задаем разрешение экрана

	win =  pygame.display.set_mode(display, DOUBLEBUF | OPENGL)		#Задаем параметры окна программы
	pygame.display.set_caption('Maze runner')						#Задаем название окна

	glMatrixMode(GL_PROJECTION)
	gluPerspective(60, (display[0] / display[1]), 0.1, 150.0)		#Задаем параметры перспективы в градусах
	glMatrixMode(GL_MODELVIEW)										

	glTranslatef(-4,-5,-4)												#Задаем начальное положение игрока
	glRotatef(0,0,0, 0)											#Задаем начальный поворот камеры

	'''Технические переменные'''
	current_mv_mat = (GLfloat * 16)()								#Получение исходной матрицы
	sum_rot_updown = 3	
	rotation_speed = 5											#Контроль наклона по вертикали
	speed = 3
	
	while True:
		'''Основной цикл рендеринга'''

		for event in pygame.event.get():
			'''Перехват момента закрытия файла для последующего удаления кэша программы'''
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		'''Перехват всех действий пользователя'''
		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_ESCAPE]:
			pygame.quit()

		'''Получаем текущую матрицу и исходную'''
		glGetFloatv(GL_MODELVIEW_MATRIX, current_mv_mat)
		glLoadIdentity()

		# Rotation Right and Left
		if pressed[pygame.K_LEFT]:
			glRotatef(rotation_speed / 2, 0, -1, 0)
			

		if pressed[pygame.K_RIGHT]:
			glRotatef(rotation_speed / 2, 0, 1, 0)
			

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
			sum_rot_updown -= rotation_speed / 2
		if pressed[pygame.K_DOWN]:
			sum_rot_updown += rotation_speed / 2

		'''Обновление текущей матрицы'''		
		glPushMatrix()
		glGetFloatv(GL_MODELVIEW_MATRIX, current_mv_mat)
		glLoadIdentity()
		glRotatef(sum_rot_updown, 1, 0, 0)
		glMultMatrixf(current_mv_mat)

		'''Основной блок отрисовки'''
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		cube(0)

		glPopMatrix()				#Стираем матрицу для перерисовки
		pygame.display.flip()		#Смена кадров для плавной отрисовки
		pygame.time.delay(25)		#Время жизни одного Frame

shapes = (((0, 1),( 0, 2),( 0, 4),( 3, 7),( 3, 1),( 3, 2),( 5, 1),( 5, 4),( 5, 7),( 6, 7),( 6, 4),( 6, 2)),

			)

verticies = (((8, 0, 8),(8, 0,0),(8,-1, 8),(8,-1,0),(0, 0, 8),(0, 0,0),(0,-1, 8),(0,-1,0)),

			  )

class cube():
	'''Функция отрисовки кубов'''
	def __init__(self, i):
		'''Этот блок ответственен за заскрашивание кубов'''
		glBegin(GL_QUADS)
		glColor3fv((1, 1, 1))
		glEnd()

		'''Это отвечает за сборку кубов'''
		glBegin(GL_LINES)
		for edge in shapes[i]:
			for vertex in edge:
				glVertex3f(verticies[i][vertex][0], verticies[i][vertex][1], verticies[i][vertex][2])
		glEnd()


main()