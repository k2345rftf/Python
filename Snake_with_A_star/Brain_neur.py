import random, math

class Neuron:

	def __init__(self, num_inputs):

		self.inputs = []
		self.num_i = num_inputs
		self.weights = []

	def sigmoid(self,x):
	  return 1 / (1 + math.exp(-x))

	def setWeights(self, weights):
		self.weights = weights

	def setRandomWeights(self):
		for i in range(self.num_i):
			self.weights.append(random.random()-0.5)

	def setInputs(self, inputs):
		self.inputs = inputs

	def calculate(self, inputs):
		self.inputs = inputs
		if len(self.weights) != len(self.inputs):
			assert False
		self.rez = 0
		for i in range(len(inputs)):
			self.rez = self.rez+self.inputs[i]*self.weights[i]

		return self.sigmoid(self.rez)


	# def copy(self):

	# 	self.copy_neuron = Neuron(self.num_i)
	# 	self.copy_neuron.setWeights(self.weights)
	# 	self.copy_neuron.setInputs(self.inputs)

	# 	return self.copy_neuron


	def mutation(self):
		self.weights = []
		i = random.randint(0,self.num_i-1)
		self.weights[i] = random.random()-0.5


class Layer:

	def __init__(self, num_inputs, num_neurons):

		self.num_n = num_neurons
		self.num_i = num_inputs
		self.inputs = []

		self.neurons = []
		for i in range(self.num_n):
			a = Neuron(self.num_i)
			a.setRandomWeights()
			self.neurons.append(a)


	def setInputs(self,inputs):
		self.inputs = inputs

		for i in self.neurons:
			i.setInputs(self.inputs)

	def setNeurons(self, neurons):
		self.neurons = neurons

	def calculate(self, inputs):
		self.rez = []
		for neuron in self.neurons:
			self.rez.append(neuron.calculate(inputs))

		return self.rez

	# def copy(self):

	# 	self.copy_layer = Layer(self.num_i, self.num_n)
	# 	self.copy_layer.setNeurons(self.neurons)
	# 	self.copy_layer.setInputs(self.inputs)

	def mutation(self):
		i = random.randint(0,self.num_n)
		self.neurons[i].mutation()


class Neuronet:

	def __init__(self, num_inputs, num_outputs):

		self.num_i = num_inputs
		self.num_o = num_outputs
		self.num_l = 0

		self.inputs = []
		self.layers = []
		self.out_layer = Layer(self.num_i,self.num_o)

	def setLayers(self, layers):
		self.layers = layers

	def addLayers(self, num_layers, num_neurons_in_layers):
		self.num_l = num_layers
		self.out_layer = Layer(num_neurons_in_layers,self.num_o)
		self.layers.append(Layer(self.num_i, num_neurons_in_layers))
		for i in range(num_layers-1):
			self.layers.append(Layer(num_neurons_in_layers, num_neurons_in_layers))

	def calculate(self, inputs):
		self.rez = self.layers[0].calculate(inputs)
		i = 1
		while i<self.num_l-1:
			self.rez = self.layers[i].calculate(self.rez)
			i+=1

		self.rez = self.out_layer.calculate(self.rez)
		return self.rez

	def copy(self):
		self.copy_neuronet = Neuronet(self.num_i, self.num_o)
		self.copy_neuronet.setLayers(self.layers)

	def mutation(self):
		i = random.randint(0,self.num_l-1)
		self.layers[i].mutation()




a = Neuronet(4,3)

a.addLayers(1,1)

print(a.calculate([5,7,8,9]))




		

