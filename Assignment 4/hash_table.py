from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type=collision_type
        self.params=params
        if collision_type=="Chain" or collision_type=="Linear":
            self.table_size=params[1]
        elif collision_type=="Double":
            self.table_size=params[3]
            self.z2=params[1]
            self.c2=params[2]
        self.table=[None]*self.table_size
        self.z=params[0]
        self.load=0
        self.n=0    
        
    def char_to_number(self, char):
       
        if 'a' <= char <= 'z':
            return ord(char) - ord('a')
        elif 'A' <= char <= 'Z':
            return ord(char) - ord('A') + 26
        else:
            return 0
        # else:
        #     raise ValueError("Only Latin alphabet characters are supported")


    def hash1(self, key):
        hash_value = 0
        for i, char in enumerate(key):
            hash_value += self.char_to_number(char) * (self.z ** i)
        return hash_value % self.table_size
    def hash2(self, key):
        hash_value = 0
        for i, char in enumerate(key):
            hash_value += self.char_to_number(char) * (self.z2 ** i)
        return self.c2- (hash_value % self.c2)
    
    def double_hash(self, key,i ):
        return (self.hash1(key) + i * self.hash2(key)) % self.table_size
        
    def insert(self, x):
        if (self.collision_type=="Linear" or self.collision_type=="Double") and self.n==self.table_size:
            raise Exception("Table is full")
        index=self.get_final_slot(x)
        if self.collision_type=="Chain":
            # print(index)
            if self.table[index] is None: 
                self.table[index]=[]
            if self.find(x)==False:
                self.table[index].append(x)
                self.n+=1
        elif self.table[index] is None:
            self.n+=1
            self.table[index]=x
        
    
    def find(self, key):
        index=self.get_final_slot(key)
        if self.collision_type=="Chain":
            if self.table[index] is None:
                return False
            # else:
            #     for keys in self.table[index]:
            #         if keys==key:
            #             return True
            #     return False
            
            for keys in self.table[index]:
                if keys==key:
                    return True
            return False
        else :
            if self.table[index] is None:
                return False
            else:
                return True
            
        
    def get_slot(self, key):
        return self.hash1(key)
    
    def get_load(self):
        return self.n/self.table_size
        pass
    
    #  def __str__(self):
        result=[]
        if self.collision_type=="Chain":
            j=0
            for i in range(self.table_size):
                if j<len(self.table)-1:
                    if self.table[i]!=None:
                        n=0
                        for keys in self.table[i]:
                            if n<len(self.table[i])-1:
                                result.append(str(keys))
                                result.append(" ; ")
                                # print(keys,";",end=" ")
                            elif n==len(self.table[i])-1:
                                result.append(str(keys))
                                result.append(" | ")
                                # print(keys," |",end=" ")
                            n+=1
                    elif self.table[i] is None:
                        result.append("<EMPTY> | ")
                        # print("<EMPTY> |",end=" ")
                elif j==len(self.table)-1:
                    if self.table[i]!=None:
                        n=0
                        for keys in self.table[i]:
                            if n<len(self.table[i])-1:
                                result.append(str(keys))
                                result.append(" ; ")
                                # print(keys," ;",end=" ")
                            elif n==len(self.table[i])-1:
                                result.append(str(keys))
                                # print(keys)
                            n+=1
                    elif self.table[i] is None:
                        result.append("<EMPTY>")
                        # print("<EMPTY>")
                j+=1
        else:
            j=0
            for i in range(self.table_size):
                if j<len(self.table)-1:
                    if self.table[i]!=None:
                        result.append(str(self.table[i]))
                        result.append(" | ")
                        # print(self.table[i]," |",end=" ")
                    elif self.table[i] is None:
                        result.append("<EMPTY> | ")
                        # print("<EMPTY> |",end=" ")
                elif j==len(self.table)-1:
                    if self.table[i]!=None:
                        result.append(str(self.table[i]))
                        # print(self.table[i])
                    elif self.table[i] is None:
                        result.append("<EMPTY>")
                        # print("<EMPTY>")
                j+=1    
        return "".join(result)
    def __str__(self):
        result = []
        if self.collision_type == "Chain":
            j = 0
            for i in range(self.table_size):
                if j < len(self.table) - 1:
                    if self.table[i] is not None:
                        n = 0
                        for keys in self.table[i]:
                            if n < len(self.table[i]) - 1:
                                result.append(str(keys))
                                result.append(" ; ")
                            elif n == len(self.table[i]) - 1:
                                result.append(str(keys))
                                result.append(" | ")
                            n += 1
                    elif self.table[i] is None:
                        result.append("<EMPTY> | ")
                elif j == len(self.table) - 1:
                    if self.table[i] is not None:
                        n = 0
                        for keys in self.table[i]:
                            if n < len(self.table[i]) - 1:
                                result.append(str(keys))
                                result.append(" ; ")
                            elif n == len(self.table[i]) - 1:
                                result.append(str(keys))
                            n += 1
                    elif self.table[i] is None:
                        result.append("<EMPTY>")
                j += 1
        else:
            j = 0
            for i in range(self.table_size):
                if j < len(self.table) - 1:
                    if self.table[i] is not None:
                        result.append(str(self.table[i]))
                        result.append(" | ")
                    elif self.table[i] is None:
                        result.append("<EMPTY> | ")
                elif j == len(self.table) - 1:
                    if self.table[i] is not None:
                        result.append(str(self.table[i]))
                    elif self.table[i] is None:
                        result.append("<EMPTY>")
                j += 1
        return "".join(result)
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        # alpha = self.get_load()
        # new_size = get_next_size()
        # new_table = [None] * new_size
        # old_table = self.table.copy()
        # self.table = new_table
        # self.table_size = new_size 
        # self.n=0
        # for i in range(len(old_table)):
        #     if old_table[i]!=None:
        #         if self.collision_type=="Chain":
        #             for keys in old_table[i]:
        #                 self.insert(keys)
        #         else:
        #             self.insert(old_table[i])
        
        pass
    def get_final_slot(self,key):
        # if self.n==self.table_size:
        #     raise Exception("Table is full")
        hash1=self.hash1(key)
        if self.collision_type=="Chain":
            return hash1
        elif self.collision_type=="Linear":
            i=0
            while self.table[(hash1+i)%self.table_size]!=None:
                if self.table[(hash1+i)%self.table_size]==key:
                    return (hash1+i)%self.table_size
                i+=1
            return (hash1+i)%self.table_size
        elif self.collision_type=="Double":
            hash2 = self.hash2(key)
            i=0
            while self.table[(hash1 + i * hash2) % self.table_size]!=None:
                if self.table[(hash1 + i * hash2) % self.table_size]==key:
                    return (hash1 + i * hash2) % self.table_size
                
                i+=1
            return (hash1 + i * hash2) % self.table_size
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    
    def insert(self, key):
        super().insert(key)
        
    
    def find(self, key):
        return super().find(key)
        
    
    def get_slot(self, key):
        return super().get_slot(key)
        
    
    def get_load(self):
        return super().get_load()
        
    
    def __str__(self):
        return super().__str__()
        
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    
    def insert(self, x):
        # super().insert(x)
        if (self.collision_type=="Linear" or self.collision_type=="Double") and self.n==self.table_size:
            raise Exception("Table is full")
        index=self.get_final_slot_map(x[0])
        if self.collision_type=="Chain":
            
            if self.table[index] is None: 
                self.table[index]=[]
            found=self.find(x[0])
            if found is None:
                self.table[index].append(x)
                self.n+=1
            # elif found!=x[1]:
            #     # for tuple in self.table[index]:
            #     #     if tuple[0]==x[0]:
            #     #         tuple[1]=x[1]
            #     for i, tuple in enumerate(self.table[index]):
            #         if tuple[0] == x[0]:
            #             self.table[index][i] = (x[0], x[1]) 
        else:
            # if self.n==self.table_size:
            #     raise Exception("Table is full")
            if self.table[index] is None:
                self.n+=1
                self.table[index]=x
                # print(x[0],index)
            else:
                self.table[index][1]=x[1]
        # x = (key, value)
        
    
    def find(self, key):
        # super().find(key)
        index=self.get_final_slot_map(key)
        # print(index)
        if self.collision_type=="Chain":
            if self.table[index] is None:
                return None
            else:
                for keys in self.table[index]:
                    if keys[0]==key:
                        return keys[1]
                return None
        else :
            if self.table[index] is None:
                return None
            else:
                return self.table[index][1]
        
    
    def get_slot(self, key):
        return super().get_slot(key)
        
    
    def get_load(self):
        return super().get_load()
        
    
    def __str__(self):
        result = []
        if self.collision_type == "Chain":
            j = 0
            for i in range(self.table_size):
                if j < len(self.table) - 1:
                    if self.table[i] is not None:
                        n = 0
                        for keys in self.table[i]:
                            if n < len(self.table[i]) - 1:
                                result.append("(")
                                result.append(str(keys[0]))
                                result.append(", ")
                                # result.append(" ; ")
                                result.append(str(keys[1]))
                                result.append(") ; ")
                            elif n == len(self.table[i]) - 1:
                                result.append("(")
                                result.append(str(keys[0]))
                                result.append(", ")
                                # result.append(" ; ")
                                result.append(str(keys[1]))
                                result.append(") | ")
                                # result.append(str(keys))
                                # result.append(" | ")
                            n += 1
                    elif self.table[i] is None:
                        result.append("<EMPTY> | ")
                elif j == len(self.table) - 1:
                    if self.table[i] is not None:
                        n = 0
                        for keys in self.table[i]:
                            if n < len(self.table[i]) - 1:
                                # result.append(str(keys))
                                # result.append(" ; ")
                                result.append("(")
                                result.append(str(keys[0]))
                                result.append(", ")
                                # result.append(" ; ")
                                result.append(str(keys[1]))
                                result.append(") ; ")
                            elif n == len(self.table[i]) - 1:
                                result.append("(")
                                result.append(str(keys[0]))
                                result.append(", ")
                                # result.append(" ; ")
                                result.append(str(keys[1]))
                                result.append(")")
                                # result.append(str(keys))
                            n += 1
                    elif self.table[i] is None:
                        result.append("<EMPTY>")
                j += 1
        else:
            j = 0
            for i in range(self.table_size):
                if j < len(self.table) - 1:
                    if self.table[i] is not None:
                        # result.append(str(self.table[i]))
                        # result.append(" | ")
                        result.append("(")
                        result.append(str(self.table[i][0]))
                        result.append(", ")
                        # result.append(" ; ")
                        result.append(str(self.table[i][1]))
                        result.append(") | ")
                    elif self.table[i] is None:
                        result.append("<EMPTY> | ")
                elif j == len(self.table) - 1:
                    if self.table[i] is not None:
                        # result.append(str(self.table[i]))
                        result.append("(")
                        result.append(str(self.table[i][0]))
                        result.append(", ")
                        # result.append(" ; ")
                        result.append(str(self.table[i][1]))
                        result.append(")")
                    elif self.table[i] is None:
                        result.append("<EMPTY>")
                j += 1
        return "".join(result)
        # return super().__str__()
    
    def get_final_slot_map(self,key):
        hash1=self.hash1(key)
        if self.collision_type=="Chain":
            return hash1
        elif self.collision_type=="Linear":
            i=0
            while self.table[(hash1+i)%self.table_size]!=None:
                if self.table[(hash1+i)%self.table_size][0]==key:
                    return (hash1+i)%self.table_size
                i+=1
            return (hash1+i)%self.table_size
        elif self.collision_type=="Double":
            hash2 = self.hash2(key)
            i=0
            while self.table[(hash1 + i * hash2) % self.table_size]!=None:
                if self.table[(hash1 + i * hash2) % self.table_size][0]==key:
                    return (hash1 + i * hash2) % self.table_size
                i+=1
            return (hash1 + i * hash2) % self.table_size    