#for rosenbrock function
import math
import random
import numpy as np

def simu_anneal(f,x_o,tol,alpha):
	x=x_o
	diff=tol+10
	T=1
	while diff>tol:
		x1=np.random.rand(2)
		x_new=np.divide(x1,math.sqrt(x1[0]**2+x1[1]**2))
		e1=f(x)
		e2=f(x_new)
		p=math.exp((e1-e2)/(alpha*T))
		pval=random.random()
		if e2<e1:
			x=x_new
		else:
			if p>pval:
				x=_new
	return x

	
