class Graf:

	def __init__(self, width, height, snake_size):

		self.width = width//snake_size
		self.height = height//snake_size
		self.walls = []
# Устанавливаем стенки(по идее стенки - тело змейки, ну или ее можно заставить
# 	искать еду не в пустом квадратике)
	def setWalls(self,walls):
		self.walls = walls

# Проверяем, принадлежит ли точка графу
	def in_bound(self, dot):
		(x,y) = dot
		return (0<=x<self.width) and (0<=y<self.height)
# Проверяем, не является ли данная точка стенкой
	def possible(self, dot):
		(x,y) = dot
		if (x,y) in self.walls:
			return False
		return True
# Вычисляем цену перехода в эту точку
	def cost(self,dot):
		if self.possible(dot):
			return 1
		return 99999999999

	def is_neibors(self, dot1, dot2):
		(x,y) = dot1
		(x1,y1) = dot2

		if abs(x-x1)>1 or abs(y-y1)>0:
			return False
		return True
# Выводим соседние точеки		
	def neibors(self, dot):
		rez = []
		(x,y) = dot
		if self.in_bound((x+1,y)):
			rez.append((x+1,y))
		if self.in_bound((x,y+1)):
			rez.append((x,y+1))
		if self.in_bound((x,y-1)):
			rez.append((x,y-1))
		if self.in_bound((x-1,y)):
			rez.append((x-1,y))

		return rez