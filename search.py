import networkx as nx
from stack import ArrayStack
from queue import ArrayQueue
import matplotlib.pyplot as plt

def DFS(G, a):
	status={}
	for node in G.nodes():
		status[node]='U'
	nodes=ArrayStack()
	nodes.push(a)
	status[a]='V'
	while nodes.isempty()==False:
		pnode=nodes.pop()
		status[pnode]='P'
		print(pnode)
		for node in G.neighbors(pnode):
			if status[node]=='U':
				nodes.push(node)
				status[node]='V'
	return

def BFS(G, a):
	status={}
	for node in G.nodes():
		status[node]='U'
	nodes=ArrayQueue()
	nodes.enqueue(a)
	status[a]='V'
	while nodes.is_empty()==False:
		pnode=nodes.dequeue()
		for node in G.neighbors(pnode):
			if status[node]=='U':
				nodes.enqueue(node)
				status[node]='V'
		status[pnode]='P'
		print(pnode)
	return


if __name__ == '__main__':
	G=nx.Graph()
	G.add_edge('a','b')
	G.add_edge('a','c')
	G.add_edge('a','d')
	G.add_edge('b','e')
	G.add_edge('b','f')
	G.add_edge('c','f')
	G.add_edge('d','g')
	G.add_edge('d','h')
	print (DFS(G,'a'))
	print (BFS(G,'a'))

