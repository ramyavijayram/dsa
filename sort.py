def SelectionSort(array):
	n=len(array)
	for i in range (n):
		k=i
		for j in range (i+1,n):
			if array[j]<array[k]:
				k=j
			array[i],array[k]=array[k],array[i]
	return array

def BubbleSort(array):
	n=len(array)
	for i in range (n-1):
		swapped=False
		for j in range (n-1-i):
			if array[j]>array[j+1]:
				array[j],array[j+1]=array[j+1],array[j]
				swapped=True
		if not swapped:
			break
	return array

def InsertionSort(array):
	n=len(array)
	for i in range (1,n):
		for j in range (i, 0, -1):
			if array[j]<array[j-1]:
				array[j],array[j-1]=array[j-1],array[j]
			else:
				break
	return array


def MergeSort(array):
	n=len(array)
	if (len(array)==1):
		return array
	else:
		return merge(MergeSort(array[:n//2]),MergeSort(array[n//2:]))

def merge(a,b):
	c=[None]*(len(a)+len(b))
	i=j=k=0
	while (i<len(a)) and (j<len(b)):
		if a[i]<b[j]:
			c[k]=a[i]
			i+=1
		else:
			c[k]=b[j]
			j+=1
		k+=1
	if (i<len(a)):
		c[k:]=a[i:]
	else:
		c[k:]=b[j:]
	return c

