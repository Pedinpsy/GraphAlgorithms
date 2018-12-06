import graph as g

grafo = g.Graph()

# grafo.insertAresta(2,0,10)
# grafo.insertAresta(2,3,10)
# grafo.insertAresta(2,4,10)
# grafo.insertAresta(3,4,10)
# grafo.insertAresta(0,4,10)
# grafo.insertAresta(3,5,10)
# grafo.insertAresta(4,2,10)
# #grafo.insertAresta(5,3,10)
# grafo.insertAresta(4,5,10)
# grafo.insertAresta(0,1,10)
# grafo.insertAresta(4,1,10)
# grafo.insertAresta(5,1,10)


grafo.insertAresta(0,1,10)
grafo.insertAresta(1,2,10)
grafo.insertAresta(2,3,10)
grafo.insertAresta(3,4,10)
grafo.insertAresta(4,2,10)
grafo.insertAresta(4,5,10)
grafo.insertAresta(5,6,10)
grafo.insertAresta(6,7,10)
grafo.insertAresta(7,5,10)
#aux =  grafo.getVertice(2)
#for i in aux.adj:
#	i.cor = "joao"
#	grafo.getVertice(i.id).cor = "asd"
#
#aux = grafo.getVertices()
#for i in aux:
#	print(i.cor)

#print(grafo.getVertices())

#grafo.dfs(0)


#print("\n\n bfs")
#grafo.bfs(0)

grafo.ciclos()