# -*- coding: utf-8 -*-
"""
Graph Model without Culmination Point

@author: Thomas Treml (datadonk23@gmail.com)
Date: 13.02.2015
"""

import networkx as net
import matplotlib.pyplot as plt

# Gerichteter Graph
G = net.DiGraph()

# node A
G.add_edge("A", "G", weight=5)
G.add_edge("A", "B", weight=100)

# node B
G.add_edge("B", "H", weight=9)
G.add_edge("B", "A", weight=100)
G.add_edge("B", "C", weight=100)

# node C
G.add_edge("C", "F", weight=1)
G.add_edge("C", "B", weight=100)
G.add_edge("C", "D", weight=100)

# node D
G.add_edge("D", "E", weight=8)
G.add_edge("D", "C", weight=100)
G.add_edge("D", "I", weight=100)

# node E
G.add_edge("E", "D", weight=2)
G.add_edge("E", "F", weight=100)

# node F
G.add_edge("F", "S", weight=7)
G.add_edge("F", "E", weight=100)
G.add_edge("F", "G", weight=100)

# node G
G.add_edge("G", "A", weight=4)
G.add_edge("G", "F", weight=100)
G.add_edge("G", "H", weight=100)

# node H
G.add_edge("H", "C", weight=3)
G.add_edge("H", "G", weight=100)
G.add_edge("H", "I", weight=100)

# node I
G.add_edge("I", "B", weight=6)
G.add_edge("I", "H", weight=100)
G.add_edge("I", "D", weight=100)


# Drawing

plot1 = plt.figure()
ax1 = plot1.add_subplot(111)
pos = net.spring_layout(G)
net.draw(G, pos=pos)
net.draw_networkx_labels(G, pos=pos)


# Routing Algorithm
def best_route(graph=G):
    """Finds best combination (from most to least exhausting) of cyling 
       ascendends in given weighted graph
    In: graph
    Out: list of path tuples past by best track
    """
    route = []
    
    nextN = sorted(graph.edges(data=True), key= lambda edge: edge[2])
    start = nextN[0][0]
    target = nextN[0][1]
    path = net.dijkstra_path(graph, start, target)
    route.append(path)        
    graph.remove_edge(path[0], path[1])
# FIXME find next node
    
    """while (len(graph) > 1):
        nextN = sorted(graph.edges(data=True), key= lambda edge: edge[2])[0][0]
        asc = net.dijkstra_path(graph, nextN, culm)
        graph.remove_node(asc[0])
        route.append(asc)
        
        if (len(graph.edges()) > 2):
            nextN = sorted(graph.edges(data=True),
                           key= lambda edge: edge[2])[1][0]
            dsc = net.dijkstra_path(graph, culm, nextN)
            route.append(dsc)
        elif (len(graph.edges()) > 1):
            nextN = sorted(graph.edges(data=True),
                           key= lambda edge: edge[2])[0][0]
            dsc = net.dijkstra_path(graph, culm, nextN)
            route.append(dsc)
    
    asc_top = ("X", "S")    
    route.append(asc_top)
    """
    return route
    
route = best_route()
