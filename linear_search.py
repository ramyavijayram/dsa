#linear search time
from time import perf_counter
import random

def linear_search(l,n):
	for number in l:
		if number==n:
			return (True)
		else:
			pass
	return (False)

size=[10**i for i in range(4,8)]
t=[]
for x in size:
	l=[random.randint(0,x) for i in range(x)]
	n=random.randint(0,x)
	t1=perf_counter()
	linear_search(l,n)
	t2=perf_counter()
	t.append(1000*(t2-t1))
print(t)

import matplotlib.pyplot as plt

plt.plot(size,t)
plt.title('Linear Search Times')
plt.xlabel('Problem size')
plt.ylabel('t')
plt.show()

