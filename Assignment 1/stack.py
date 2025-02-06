class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
         self._data=[] #nonpubliclist instance
 
    def len(self):
        return len(self._data)
 
    def is_empty(self):
        return len(self._data)==0
 
    def push(self,e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1] 
 
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
        
    # You can implement this class however you like
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass