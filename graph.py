class Vertice:
	def __init__(self, id, cor = 'branco'):
		self.id = id
		self.cor = cor
		self.adj = []
	def __str__(self):
		return self.id
	def __repr__(self):
		return str(self.id)

	def setAdjacentes(self, adjacentes):
		self.adj = adj.concat(adjacentes)
	
	def serAdjacente(self, adjacente):
		self.adj.append(adjacente)


class Aresta:
	def __init__(self,peso,origem,adjacente):
		self.origem = origem
		self.adj = adjacente
		self.peso = peso



class Graph:
	def __init__(self, dic = True):
		self.vertices = []
		self.arestas = []
		self.direcionado = dic
	def getVertices(self):
		return self.vertices

	def getVertice(self,a):
		for i in self.vertices:
			print(i.id,a)
			if i.id == a:
				return i
		return False

	def insertAresta(self,a,b,peso):
		aux = True
		origem = self.getVertice(a)
		adj = self.getVertice(b)

		if (origem  == False):
			origem = Vertice(a)
			self.vertices.append(Vertice(a))
		if(adj == False):
			origem = Vertice(b)
			self.vertices.append(Vertice(b))
		origem.serAdjacente(adj)

		self.arestas.append(Aresta(origem,adj,peso))

