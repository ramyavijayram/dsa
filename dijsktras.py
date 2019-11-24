import networkx as nx
from priqueue import PriorityQueue

def Dijsktra(G, source):
	nodes=PriorityQueue()
	boxes={}
	status={}
	for node in G.nodes():
		status[node]='U'
	for node in G.nodes():
		boxes[node]='None'
	nodes.put(source,0)
	status[source]='V'
	while nodes.is_empty()==False:
		vertex=nodes.get()
		centre=vertex[0]
		boxes[centre]=vertex[1]
		status[centre]='P'
		for neighbour in G.neighbors(centre):
			if status[neighbour]=='V':
				value=(G[centre][neighbour]['weight']+boxes[centre])
				if value<nodes.view(neighbour):
					waste=nodes.get()
					nodes.put(neighbour,value)
			if status[neighbour]=='U':
				nodes.put(neighbour,(G[centre][neighbour]['weight'])+boxes[centre])
				status[neighbour]='V'
	return [(key, value) for key, value in boxes.items()]

G=nx.Graph()
G.add_edge('A','B',weight=1.0)
G.add_edge('A','D',weight=5.0)
G.add_edge('A','C',weight=2.0)
G.add_edge('B','C',weight=3.0)
G.add_edge('C','D',weight=1.0)
G.add_edge('E','D',weight=1.0)
G.add_edge('C','E',weight=2.0)

print (Dijsktra(G, 'A'))

