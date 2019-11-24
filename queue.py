class ArrayQueue:   
    
    def __init__(self):
        self._front=0
        self._size=0
        self._data=[None]*10
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        """Return True if Queue is empty"""
        return self._size==0
    
    def dequeue(self):
        if self.is_empty()==True:
            raise Exception('Empty Queue')
        else:
            ans=self._data[self._front]
            self._data[self._front]==None
            self._front=(self._front+1)%len(self._data)
            self._size-=1
            return ans

    def resize(self,cap):
        old=self._data  
        self._data=[None]*(cap)
        walk=self._front
        for i in range(self._size):
            self._data[i]=old[walk]
            walk=(walk+1)%len(old)
        self._front=0

    
    def enqueue(self, e):
        if self._size==len(self):
            self.resize(2*len(self._data))
        new=(self._front + self._size)%len(self._data)
        self._data[new]=e
        self._size+=1

            