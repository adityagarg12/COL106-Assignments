import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.book_titles = book_titles
        self.texts = texts
        self.books=[]
        for i in range (len(book_titles)):
            self.books.append(Book(book_titles[i],texts[i]))
            
        self.mergeSort(self.books,0,len(self.books)-1,self.comp)
        
        
    def comp(self,a,b):
        if a.book_title <= b.book_title:
            return 1
        else:
            return 0
    def search_comp(self,a,b):
        if a.book_title<b:
            return 1
        elif a.book_title>b:
            return -1
        else:
            return 0
    def search_comp2(self,a,b):
        if a<b:
            return 1
        elif a>b:
            return -1
        else:
            return 0   
    def binary_search(self,arr, target,comp):
    
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if comp(arr[mid],target)==0:
                return mid
            elif comp(arr[mid],target)>0:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

    def merge(self,arr, l, m, r,comp):
        n1 = m - l + 1
        n2 = r - m
    
        Left = [0] * (n1)
        Right = [0] * (n2)
    
        for i in range(0, n1):
            Left[i] = arr[l + i]
    
        for j in range(0, n2):
            Right[j] = arr[m + 1 + j]
    
        i = 0     
        j = 0     
        k = l    
    
        while i < n1 and j < n2:
            if comp(Left[i],Right[j])>0:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = Left[i]
            i += 1
            k += 1
    
        while j < n2:
            arr[k] = Right[j]
            j += 1
            k += 1
    
 
    def mergeSort(self,arr, l, r,comp):
        if l < r:
    
           
            m = l+(r-l)//2
            self.mergeSort(arr, l, m,comp)
            self.mergeSort(arr, m+1, r,comp)
            self.merge(arr, l, m, r,comp)


    def distinct_words(self, book_title):
        book=self.books[self.binary_search(self.books,book_title,self.search_comp)]
        return book.distinct_words
        pass
    
    def count_distinct_words(self, book_title):
        book=self.books[self.binary_search(self.books,book_title,self.search_comp)]
        return len(book.distinct_words)

        pass
    
    def search_keyword(self, keyword):
        keyword_books=[]
        for book in self.books:
            if self.binary_search(book.distinct_words,keyword,self.search_comp2)!=-1:
                keyword_books.append(book.book_title)
        return keyword_books
        pass
    
    def print_books(self):
        for book in self.books:
            print(book.book_title,end=": ")
            i=0
            for word in book.distinct_words:
                
                if i<len(book.distinct_words)-1:
                    print(word,"|",end=" ")
                    i+=1
                elif i==len(book.distinct_words)-1:
                    print(word) 
            
        

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
       
        self.name = name
        self.params=params
        if name=="Jobs":
            
            self.hash_set=ht.HashSet("Chain",params)
            self.hash_map=ht.HashMap("Chain",params)
        elif name=="Gates":
            self.hash_set=ht.HashSet("Linear",params)
            self.hash_map=ht.HashMap("Linear",params)
        elif name=="Bezos":
            self.hash_set=ht.HashMap("Double",params)
            self.hash_map=ht.HashMap("Double",params)
        
    
    def add_book(self, book_title, text):
        book=JBGL_Book(book_title,text)

        # self.hash_map.insert((book_title,text))
        if self.name=="Jobs":
            
            hash_set=ht.HashSet("Chain",self.params)
        elif self.name=="Gates":
            hash_set=ht.HashSet("Linear",self.params)
        elif self.name=="Bezos":
            hash_set=ht.HashSet("Double",self.params)
        for word in text:
            hash_set.insert(word)
        # book=JBGL_Book(book_title,text)
        book.hash_set=hash_set
        self.hash_map.insert((book_title,book))
        
    
    def distinct_words(self, book_title):
        book=self.hash_map.find(book_title)
        distinct_words=[]
        # book=JBGL_Book(book_title,text)
        if book is None:
            return []
        hash_set = book.hash_set
        if self.name=="Jobs":
            for slot in hash_set.table:
                if slot is not None:
                    for word in slot:
                        if word is not None:
                            distinct_words.append(word)
        elif self.name=="Gates" or self.name=="Bezos":
            for slot in hash_set.table:
                if slot is not None:
                    distinct_words.append(slot)   
        
        return distinct_words   
        pass
    
    def count_distinct_words(self, book_title):
        book=self.hash_map.find(book_title)
        # book=JBGL_Book(book_title,text)
        hash_set = book.hash_set
        return hash_set.n
    
        pass
    
    def search_keyword(self, keyword):
        keyword_books=[]
        # for book in self.books:
        #     if self.binary_search(book.distinct_words,keyword,self.search_comp2)!=-1:
        #         keyword_books.append(book.book_title)
        if self.name=="Jobs":
            for slot in self.hash_map.table:
                if slot is not None:
                    for book_title in slot:
                        if book_title is not None:
                            book=self.hash_map.find(book_title[0])
                            # book=JBGL_Book(book_title,text)
                            hash_set = book.hash_set
                            found_keyword=hash_set.find(keyword)
                            if found_keyword == True:
                                keyword_books.append(book_title[0])
                            
        elif self.name=="Gates" or self.name=="Bezos":
            for book_title in self.hash_map.table:
                if book_title is not None:
                    book=self.hash_map.find(book_title[0])
                    # book=JBGL_Book(book_title,text)
                    hash_set = book.hash_set
                    found_keyword=hash_set.find(keyword)
                    if found_keyword == True:
                        keyword_books.append(book_title[0])
                    
        return keyword_books
        pass
    
    def print_books(self):
        collison_type=self.hash_map.collision_type
        if collison_type=="Chain":
            for slot in range(self.hash_map.table_size):
                if self.hash_map.table[slot]!=None:
                    for book in self.hash_map.table[slot]:
                        print(book[0],end=": ")
                        j=0
                        for i in range(book[1].hash_set.table_size):
                            if j<len(book[1].hash_set.table)-1:
                                if book[1].hash_set.table[i]!=None:
                                    n=0
                                    for keys in book[1].hash_set.table[i]:
                                        if n<len(book[1].hash_set.table[i])-1:
                                            # result.append(str(keys))
                                            # result.append(" ; ")
                                            print(keys,";",end=" ")
                                        elif n==len(book[1].hash_set.table[i])-1:
                                            # result.append(str(keys))
                                            # result.append(" | ")
                                            print(keys,"|",end=" ")
                                        n+=1
                                elif book[1].hash_set.table[i] is None:
                                    # result.append("<EMPTY> | ")
                                    print("<EMPTY> |",end=" ")
                            elif j==len(book[1].hash_set.table)-1:
                                if book[1].hash_set.table[i]!=None:
                                    n=0
                                    for keys in book[1].hash_set.table[i]:
                                        if n<len(book[1].hash_set.table[i])-1:
                                            # result.append(str(keys))
                                            # result.append(" ; ")
                                            print(keys,";",end=" ")
                                        elif n==len(book[1].hash_set.table[i])-1:
                                            # result.append(str(keys))
                                            print(keys)
                                        n+=1
                                elif book[1].hash_set.table[i] is None:
                                    # result.append("<EMPTY>")
                                    print("<EMPTY>")
                            j+=1
        else:
            for slot in range(self.hash_map.table_size):
                if self.hash_map.table[slot]!=None:
                    book=self.hash_map.table[slot]
                    print(book[0],end=": ")
                    j=0
                    for i in range(book[1].hash_set.table_size):
                        if j<len(book[1].hash_set.table)-1:
                            if book[1].hash_set.table[i]!=None:
                                # result.append(str(book[1].hash_set.table[j]))
                                # result.append(" | ")
                                print(book[1].hash_set.table[i],"|",end=" ")
                            elif book[1].hash_set.table[i]==None:
                                # result.append("<EMPTY> | ")
                                print("<EMPTY> |",end=" ")
                        elif j==len(book[1].hash_set.table)-1:
                            if book[1].hash_set.table[i]!=None:
                                # result.append(str(book[1].hash_set.table[j]))
                                print(book[1].hash_set.table[i])
                            elif book[1].hash_set.table[i]==None:
                                # result.append("<EMPTY>")
                                print("<EMPTY>")
                        j+=1    
                    # return "".join(result)
        
class JBGL_Book:
    def __init__(self,book_title,texts):
        self.book_title = book_title
        self.words = texts
        self.hash_set=None
        # self.merge_sort(self.words,self.comp2)
        
class Book:
    def __init__(self,book_title,texts):
        self.book_title = book_title
        self.words = texts.copy()
        # self.merge_sort(self.words,self.comp2)
        self.mergeSort(self.words,0,len(texts)-1,self.comp2)
        self.distinct_words = []
        self.distinct_words.append(self.words[0])
        for i in range(1,len(texts)):
            if self.words[i] != self.words[i-1]:
                self.distinct_words.append(self.words[i])
    def comp2(self,a,b):
        if a <= b:
            return 1
        else:
            return 0
 
    def merge(self,arr, l, m, r,comp):
        n1 = m - l + 1
        n2 = r - m     
        Left = [0] * (n1)
        Right = [0] * (n2)     
        for i in range(0, n1):
            Left[i] = arr[l + i]
    
        for j in range(0, n2):
            Right[j] = arr[m + 1 + j]       
        i = 0     
        j = 0    
        k = l     
        while i < n1 and j < n2:
            if comp(Left[i],Right[j])>0:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1      
        while i < n1:
            arr[k] = Left[i]
            i += 1
            k += 1      
        while j < n2:
            arr[k] = Right[j]
            j += 1
            k += 1
    def mergeSort(self,arr, l, r,comp):
        if l < r:        
            m = l+(r-l)//2           
            self.mergeSort(arr, l, m,comp)
            self.mergeSort(arr, m+1, r,comp)
            self.merge(arr, l, m, r,comp)
 
    

