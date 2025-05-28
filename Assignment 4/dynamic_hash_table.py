from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        new_size = get_next_size()
        new_table = [None] * new_size
        old_table = self.table.copy()
        self.table = new_table
        self.table_size = new_size 
        self.n=0
        for i in range(len(old_table)):
            if old_table[i]!=None:
                if self.collision_type=="Chain":
                    for keys in old_table[i]:
                        if keys is not None:
                            self.insert(keys)
                else:
                    
                    self.insert(old_table[i])
        # IMPLEMENT THIS FUNCTION
        
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        new_size = get_next_size()
        new_table = [None] * new_size
        old_table = self.table.copy()
        self.table = new_table
        self.table_size = new_size 
        self.n=0
        for i in range(len(old_table)):
            if old_table[i]!=None:
                if self.collision_type=="Chain":
                    for keys in old_table[i]:
                        if keys is not None:
                            self.insert(keys)
                            
                else:
                    
                    self.insert(old_table[i])
        # IMPLEMENT THIS FUNCTION
        
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()