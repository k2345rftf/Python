# Импортируем библиотеку, в которой реализована так называемая куча
import random, time

from Brains import A_star
from Graf import Graf



# Создаем граф, по которому будет ходить змейка(по сути это просто сетка,
# 	в которой хранятся центры квадратиков, длинна граней в квадратиках равна ширине змейки)








class Surface:

	def __init__(self, graf):
		self.graf = graf
		self.snake = Snake(self.graf)
		self.food = ()
		self.create_food()
		# print(self.food)
		self.tt = self.snake.get_snake()
		if len(self.tt) > 1:
			self.graf.setWalls(self.tt[1:len(self.tt)])

		self.running = True

	def run(self):
		while self.running:
			self.game_rule()
			self.draw()
			self.update()

	def create_food(self):
		self.x = random.randint(0,self.graf.width-1)
		self.y = random.randint(0,self.graf.height-1)
		while (self.x,self.y) in self.snake.snake:
			self.x = random.randint(0,self.graf.width-1)
			self.y = random.randint(0,self.graf.height-1)
		self.food = (self.x,self.y)



	def game_rule(self):
		if self.snake.eat(self.food):
			self.create_food()

		if self.snake.isKilled():
			self.running = False

		self.snake.movement(self.food)

	def draw(self):
		# print(self.food)
		for i in range(self.graf.width):
			string = ''
			for j in range(self.graf.height):
				if (i,j) == self.food:
					string = string + '0'

				elif (i,j) in self.snake.snake:
					if (i,j) == self.snake.snake[0]:
						string = string + 'X'
					else:

						string = string + '#'

				else:
					string = string + '.'


			print(string)

		print()


	def update(self):
		time.sleep(0.01)


class Snake:

	def __init__(self, graf):
		self.snake = [(0,0)]
		self.snake_old = [(0,0)]
		self.snake_len = 1
		self.alive = True
		self.program = []
		self.brain = A_star()
		self.graf = graf

	def get_snake(self):
		return self.snake
	def eat(self, food):

		if self.snake[0] == food:
			self.snake.append((self.snake_old))
			self.snake_len +=1
			return True
		return False

	def movement(self, food):
		if len(self.program) == 0:
			self.graf.setWalls(self.snake)
			self.brain.calculate(self.snake[0], food, self.graf)
			self.program = self.brain.create_list()
			self.program = self.program[1:len(self.program)]
		# print(self.program)
		self.move(self.program[0])
		t = self.program[1:len(self.program)]
		self.program = []
		self.program = t

	def move(self, dot):
		if dot not in self.snake:
			t = []
			t.append(dot)
			for i in range(self.snake_len-1):
				t.append(self.snake[i])
			self.snake_old = self.snake[self.snake_len-1]

			self.snake_old =self.snake[self.snake_len-1]
			self.snake = t
		else:
			self.kill()

	def kill(self):
		self.alive = False

	def isKilled(self):
		return not self.alive


graf = Graf(150, 150,10)
# a = A_star()
# a.calculate((1, 0),(9, 7),graf)

# (came_from,cost_so_far) = a.get_data()
# print(a.create_list())

# for key,value in came_from.items():
# 	print(str(key)+":"+str(value))
surf = Surface(graf)

surf.run()

# a = input('dddd')


