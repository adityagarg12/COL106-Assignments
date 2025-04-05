'''
Python Code to implement a heap with general comparison function
'''
# from custom import item
class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self._data=init_array
        self.comparator=comparison_function
        self.build_heap()
        
    def insert(self, key):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        # item = item(key,value)
        self._data.append(key)
        self.upheap(len(self._data)-1)
        
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if self.is_empty():
            return None
        top = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()
        self.downheap(0)
        return top

        
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if self.is_empty():
            return None
        top = self._data[0]
        return top
        
    
    # You can add more functions if you want to
    def parent(self, j):
        return (j-1)//2
 
    def left(self, j):
        return 2* j+1
 
    def right(self, j):
        return 2* j+2
    
    def swap(self,i,j):
        self._data[i],self._data[j]=self._data[j],self._data[i]
    
    def upheap(self,j):
        parent=self.parent(j)
        if j>0 and self.comparator(self._data[j], self._data[self.parent(j)])>0:
            self.swap(j,parent)
            self.upheap(parent)
            
    def downheap(self, j):
        size = len(self._data)
        largest = j
        left = self.left(j)
        right = self.right(j)

        if left < size and self.comparator(self._data[left], self._data[largest])>0:
            largest = left
        if right < size and self.comparator(self._data[right], self._data[largest])>0:
            largest = right

        if largest != j:
            self._data[j], self._data[largest] = self._data[largest], self._data[j]
            self.downheap(largest)
            
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data)==0
    
    def heapify(self, n, i):
        best = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.comparator(self._data[left], self._data[best])>0:
            best = left

        if right < n and self.comparator(self._data[right], self._data[best])>0:
            best = right

        if best != i:
            self._data[i], self._data[best] = self._data[best], self._data[i]
            self.heapify(n, best)

    def build_heap(self):
        n = len(self._data)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
            
        # print(self._data)

# def load_comp(node1,node2):
#     if node1<node2:
#         return 1
#     elif node1>node2:
#         return -1
#     else:
#         return 0
# heap=Heap(load_comp,[2,8,1])
# print(heap._data)
# def min_comparison(x, y):
#     return x < y  # Min-Heap condition
    def insert_new(self, key,time):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        # item = item(key,value)
        self._data.append(key)
        self.upheap_new(len(self._data)-1,time)
        
    
    def extract_new(self,time):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if self.is_empty():
            return None
        top = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()
        self.downheap_new(0,time)
        return top

    def upheap_new(self,j,time):
        parent=self.parent(j)
        if j>0 and self.comparator(self._data[j], self._data[self.parent(j)],time)>0:
            self.swap(j,parent)
            self.upheap_new(parent,time)
            
    def downheap_new(self, j,time):
        size = len(self._data)
        largest = j
        left = self.left(j)
        right = self.right(j)

        if left < size and self.comparator(self._data[left], self._data[largest],time)>0:
            largest = left
        if right < size and self.comparator(self._data[right], self._data[largest],time)>0:
            largest = right

        if largest != j:
            self._data[j], self._data[largest] = self._data[largest], self._data[j]
            self.downheap_new(largest,time)
        