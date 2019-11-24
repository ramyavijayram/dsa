class PriorityQueue:   
    
    def __init__(self):
        self._front=0
        self._size=0
        self._data={}
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        """Return True if Queue is empty"""
        return self._size==0

    def view(self, e):
        return self._data[e]
    
    def get(self):
        if self.is_empty()==True:
            raise Exception('Empty Queue')
        else:
            pri=min(self._data[x] for x in self._data.keys())
            for key, value in self._data.items():
                if pri==value:
                    ans=key
            del self._data[ans]
            self._size-=1
            return (ans, pri)

    
    def put(self, e, weight):
        self._data[e]=weight
        self._size+=1
