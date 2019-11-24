#check time for binary search
from time import perf_counter
import random

def binary_search(l,n):
	#l.sort()
	i=int(len(l)/2)
	oldi=len(l)
	while l[i]!=n:
		if l[i]>n:
			newi=int(i/2)
		else:
			newi=int((i+oldi)/2)
		oldi=i
		i=newi
		if oldi==i:
			return False
	return True

size=[2**i for i in range(15,22)]
t=[]
for x in size:
	l=[random.randint(0,x) for i in range(x)]
	l.sort()
	n=random.randint(0,x)
	t1=perf_counter()
	binary_search(l,n)
	t2=perf_counter()
	t.append(1000*(t2-t1))
print(t)

import matplotlib.pyplot as plt
import math
sz=[math.log2(x) for x in size]
plt.plot(sz,t,'x-')
plt.title('Binary Search Times')
plt.xlabel('Log problem size')
plt.ylabel('t')
plt.show()

