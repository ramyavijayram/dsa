import networkx as nx
import matplotlib.pyplot as plt



def hypercube(n):
	nodes=[]
	G=nx.Graph()
	for x in range(2**n):
		bin1=str(bin(x))[2:]
		binary='0'*(n- len(bin1))+bin1
		nodes.append(binary)
		#print(nodes)
	for node in nodes:
		for node2 in nodes:
	 		edit= abs(int(node)-int(node2))
	 		edits=str(edit)
	 		#print (edits)
	 		if edits.count('1')==1 and edits.count('0')==(len(edits)-1):
	 			G.add_edge(node, node2)

	nx.draw(G)
	plt.show()		
	return



def regular(n,k):
	blocks=[x for x in range(n)]
	G=nx.Graph()
	for x in blocks:
		for r in range(1,k+1):
			node1=x
			node2= blocks[(x+r)%n]
			node3=blocks[x-r]
			G.add_edge(node1, node2)
			G.add_edge(node1, node3)	
	nx.draw(G)
	plt.show()		
	return

print (regular(10,4))

