import graph as g

grafo = g.Graph()

grafo.insertAresta(1,2,10)

grafo.insertAresta(1,3,10)
grafo.insertAresta(2,3,10)

print(grafo.getVertices())