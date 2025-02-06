class Node:
    def __init__(self,key,value):
        self._key=key  
        self._value=value      
        self.height = 1
        self.left = None
        self.right = None
        self._parent = None