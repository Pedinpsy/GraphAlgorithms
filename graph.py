from collections import deque
import numpy as np
import copy
import heapq as hp

class Vertice:
	def __init__(self, id, cor = 'b'):
		self.id = id
		self.cor = cor
		self.adj = []
		self.nivel = 0
		self.pai = None
		self.value = float("inf")
		self.prev = None
	def __str__(self):
		return str(self.id)
	def __repr__(self):
		return str(self.id)

	def setAdjacentes(self, adjacentes):
		self.adj = self.adj.concat(adjacentes)
	
	def setAdjacente(self, adjacente):
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
			if i.id == a:
				return i
		return False
	def getArestas(self):
		return self.arestas
	def getAresta(self,origem,destino):
		for i in self.arestas:

			if i.origem.id == origem and i.adj.id == destino:

				return i
		return None


	def insertAresta(self,a,b,peso):
		aux = True
		origem = self.getVertice(a)
		adj = self.getVertice(b)
		
		if (origem  == False):
			origem = Vertice(a)
			self.vertices.append(Vertice(a))
		if(adj == False):
			adj = Vertice(b)
			self.vertices.append(Vertice(b))
		
		origem = self.getVertice(a)
		origem.setAdjacente(adj)
	
		aux = self.getVertice(a)

		#print(origem.adj)
		self.arestas.append(Aresta(peso,origem,adj))

	def dfs(self,origem):
		pilha = deque()
		fila = []
		cilco = ()

		for i in range(len(self.vertices)):
			self.vertices[i].cor = 'b'
			self.vertices[i].nivel = 0

		#print(origem.adj)	

		fila.append(self.getVertice(origem))

		for i in sorted(self.getVertices(), key=lambda adjacentes: int(adjacentes.id)):	
			if(i not in fila):
				fila.append(self.getVertice(i.id))

		for i in fila:
			origem = self.getVertice(i.id)
			pilha.append(origem)



			while(len(pilha)>0):
				atual = pilha.pop()

				origem = self.getVertice(atual.id)
			

				for i in sorted(self.getVertice(origem.id).adj, key=lambda adjacentes: int(adjacentes.id), reverse = True):

					if self.getVertice(i.id).cor == "b":
						pilha.append(i)
						self.getVertice(i.id).pai = origem
						self.getVertice(i.id).nivel = atual.nivel+1

				origem.cor = 'c'
				self.getVertice(origem.id).cor = 'c'

				if(origem.pai != None):
					origem.nivel = self.getVertice(origem.pai.id).nivel+1

				

		for i in self.vertices:
			print("vertice :" +  str(i.id) +  " Pai : " +str( i.pai)+" Nivel :"+ str(i.nivel))



	def bfs(self, origem):
		fila = deque()
		vertices = []
		for i in range(len(self.vertices)):
			self.vertices[i].cor = 'b'
			self.vertices[i].nivel = 0
			self.vertices[i].pai = None

		aux = self.getVertice(origem)
	
		vertices.append(aux)
		vertices = vertices + self.getVertices()
		fila.append(aux)
		#for k in vertices:
			#fila.append(k)
		while(len(fila)>0):
			atual = fila.popleft()
			self.getVertice(atual.id).cor = 'c'

			adjacentes =  self.getVertice(atual.id).adj

			for i in sorted(adjacentes ,key=lambda aux: int(aux.id), reverse = True):
				aux = self.getVertice(i.id)
				if(aux.cor !='c'):			
					aux.cor = 'c'
					aux.pai = atual
					aux.nivel = atual.nivel+1
					fila.appendleft(aux)
			

		for i in self.vertices:
			print("vertice :" +  str(i.id) +  " Pai : " +str( i.pai)+" Nivel :"+ str(i.nivel))

	def DistanceMatrix(self):
		size = len(self.getVertices())
		matrix = np.zeros((size,size),dtype=np.float64)
		for i in self.getVertices():
			self.bfs(i.id)

			for k in self.getVertices():
				matrix[i.id][k.id] = k.nivel
	
				
		print(matrix)

	def countCicles(self, target, node, cycles, pilha, visitado, punish):
		if node == target:
			if len(pilha) > 0:
				cycles[node] += 1
				return True

		pilha.append(self.getVertice(node))
		#visitado[node] = 1

		for i in sorted(self.getVertice(node).adj ,key=lambda aux: int(aux.id)):
			if visitado[i.id] == 0:
				if i.id != target:
					visitado[i.id] = 1
				if punish[i.id] == 0:
					continue
				result = self.countCicles(target, i.id, cycles, copy.copy(pilha), copy.copy(visitado), punish)



		pilha.pop()
		return False


	def dfsCiclo(self,pilha,numciclo):
		#print(numciclo)
		print(pilha)
		while (len(pilha) > 0 ):
			aux = self.getVertice(pilha[len(pilha)-1].id)	
			aux.cor = 'c'
			print(pilha)
			for k in aux.adj:
				print(k.id)

			pilha.pop()

			for i in sorted(self.getVertice(aux.id).adj ,key=lambda aux: int(aux.id)):
				#print(self.getVertice(i.id).cor,pilha)
				#print(pilha,i)

				if self.getVertice(i.id).cor == 'b':
					self.getVertice(i.id).cor = 'c'
					self.getVertice(i.id).nivel = aux.nivel+1
					pilha.append(self.getVertice(i.id))
					
					self.dfsCiclo(copy.copy(pilha),numciclo)
				elif self.getVertice(i.id).cor == 'c':
					self.getVertice(i.id).cor = 'k'
					for k in pilha:
						if k.id == i.id:
							print("ciclos")

			#print(pilha)
			#if(len(pilha)>0):
			

	def ciclos(self):
		pilha = deque()
		numciclo = 0
		cycles = [0 for i in range(len(self.vertices))]
		visited = [0 for i in range(len(self.vertices))]
		punish = [1 for i in range(len(self.vertices))]
		for i in range(len(self.vertices)):
			self.countCicles(i, i, cycles, copy.copy(pilha), copy.copy(visited), punish)
			punish[i] = 0

		#self.countCicles(2, 2, cycles, copy.copy(pilha), copy.copy(visited), punish)
		#print(2, cycles)

		c = 0
	
		for i in cycles:
			if i > 0:
				c += i
		if(self.direcionado == False):
			print(c-len(self.arestas))
		print(c)	
		#print(self.dfsCiclo(pilha,numciclo))



	def dijkstra(self, origem, destino):
		vertices = []
		for i in self.getVertices():
			aux = self.getVertice(i.id)
			aux.value = float("inf")
		self.getVertice(origem).value = 0

		hp.heapify(vertices)
		hp.heappush(vertices,origem)
		while(len(vertices)>0):
			aux = hp.heappop(vertices)
			for i in self.getVertice(aux).adj:
				hp.heappush(vertices,i.id)
				og = self.getVertice(aux)
				peso = self.getAresta(aux,i.id).peso
				
				if og.value+peso < i.value:
					auxOg = self.getVertice(i.id)
				
					auxOg.value = og.value+peso
					auxOg.prev = og.id
		caminho = destino
		lista = []

		while(caminho != origem):
			if(caminho is None):
				break
			lista.append(caminho)
			caminho = self.getVertice(caminho).prev
		lista.append(caminho)
		lista.reverse()
		print("O menor caminho de", origem, "ateh" ,destino,"eh:",origem,lista )	








