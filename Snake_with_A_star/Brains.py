import heapq

from collections import deque
# Создаем класс, который определяет очередь с приоритетом.
# Т.е. в нем по сути лежит список из всех просмотренных точек
# и те точки, у которых значение пути наименьшее проверяются
# раньше тех точек, у которых значение пути(priority) наибольшее

class PriorityQueue:
	def __init__(self):
		self.elements = []
# Проверка на пустоту очереди
	def empty(self):
		return len(self.elements) == 0
# Элемент встает в очередь	
	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))
# Элемент удаляется из очереди с выводом в переменную	
	def get(self):
		return heapq.heappop(self.elements)[1]

class A_star:
	def __init__(self):
		self.queue = PriorityQueue()
		# Здесь будет храниться путь змейки
		self.came_from = {}
		# Здесь храниться стоимость(расстояние) перемещения от начала и до конца
		self.cost_of_far = {}

	def clear(self):
		self.queue = PriorityQueue()
		# Здесь будет храниться путь змейки
		self.came_from = {}
		# Здесь храниться стоимость(расстояние) перемещения от начала и до конца
		self.cost_of_far = {}


	def calculate(self, start, goal, graf):
		# print(goal)
		self.graf = graf
		self.start = start
		self.goal = goal

		
		self.queue.put(self.start,0)
		self.came_from[self.start] = None
		self.cost_of_far[self.start] = 0

		while (not self.queue.empty()):
			current = self.queue.get()
# Проверяем, а вдруг эта точка и есть искомая
			if current == self.goal:
				break
# Определяем соседние клетки
			for neib in self.graf.neibors(current):
				# print(neib)
# Вычисляем стоимость перехода из исходнай клетки в соседнюю
				next_cost = self.cost_of_far[current]+self.graf.cost(neib)
# Проверяем, рассматривали ли мы уже эту точку до этого, или нет
# Если да и общая цена пути не изменилась, или увеличилась, то просто идем дальше, ибо 
# нет смысла рассматривать данную точку
# Если нет, или общая цена пути изменилась, то
# Либо просто добавляем точку в рассматриваемые, либо изменяем общую цену пути до этой точки
				if neib not in self.cost_of_far or next_cost<self.cost_of_far[neib]:

					self.cost_of_far[neib] = next_cost
					self.priority = next_cost + self.heruis(self.goal, neib)
					self.queue.put(neib, self.priority)
					self.came_from[neib] = current
			# print("===============")
# Выводим результат
	def get_data(self):
		return (self.came_from,self.cost_of_far)
# Метрика расстояния
	def heruis(self,dot_f,dot_s):
		(x,y) = dot_s
		(x1,y1) = dot_f
		return abs((x-x1)) + abs((y-y1))

	def create_list(self):
		lists = [self.goal]
		current = self.goal
		# for key,value in self.came_from.items():
		# 	print(str(key)+":"+str(value))
		# i = 0
		while current != self.start:
			# print(i)
			current = self.came_from[current]
			lists.append(current)
			# i+=1
		lists.reverse()
		self.clear()
		return lists




# class Hamilt_way:

# 	def __init__(self):

# 		self.queue = decue()


# 	def calculate(self, graf):
		
