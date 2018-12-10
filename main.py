import graph as g

grafoDjk = g.Graph()
grafoCiclo = g.Graph()

grafoCiclo.insertAresta(2,0,10)
grafoCiclo.insertAresta(2,3,10)
grafoCiclo.insertAresta(2,4,10)
grafoCiclo.insertAresta(3,4,10)
grafoCiclo.insertAresta(0,4,10)
grafoCiclo.insertAresta(3,5,10)
grafoCiclo.insertAresta(4,2,10)
grafoCiclo.insertAresta(5,3,10)
grafoCiclo.insertAresta(4,5,10)
grafoCiclo.insertAresta(0,1,10)
grafoCiclo.insertAresta(4,1,10)
grafoCiclo.insertAresta(5,1,10)


# grafo.insertAresta(0,1,10)
# grafo.insertAresta(1,2,10)
# grafo.insertAresta(2,3,10)
# grafo.insertAresta(3,4,10)
# grafo.insertAresta(4,2,10)
# grafo.insertAresta(4,5,10)
# grafo.insertAresta(5,6,10)
# grafo.insertAresta(6,7,10)
# grafo.insertAresta(7,5,10)
# grafo.insertAresta(7,0,10)

#djikstra
grafoDjk.insertAresta(0,1,10)
grafoDjk.insertAresta(0,2,15)
grafoDjk.insertAresta(1,3,12)
grafoDjk.insertAresta(1,4,15)
grafoDjk.insertAresta(3,4,1)
grafoDjk.insertAresta(3,5,2)
grafoDjk.insertAresta(4,5,5)
grafoDjk.insertAresta(2,5,10)




#aux =  grafo.getVertice(2)
#for i in aux.adj:
#	i.cor = "joao"
#	grafo.getVertice(i.id).cor = "asd"
#
#aux = grafo.getVertices()
#for i in aux:
#	print(i.cor)

#print(grafo.getVertices())
print("\n\n DFS:")
grafoCiclo.dfs(0)


print("\n\n BFS:")

grafoCiclo.bfs(0)

print(" \n\nQuantidade de Ciclos: ")
grafoCiclo.ciclos()

print("\n\n Matriz de distancias")
grafoCiclo.DistanceMatrix()

print("\n\nDjikstra:")
grafoDjk.dijkstra(0,5)


