'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
from treasure import Treasure



class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        self.time=0
        self.crewmates = [CrewMate() for _ in range(m)]
        self.crewmates_had_treasure = []
        self.crew_load= Heap(self.load_comp,self.crewmates)
        # for i in range(m):
        #     self.crew_load.insert(self.crewmates[i])
        
        
    def load_comp(self,node1,node2):
    
        updated_load= node1.load - (self.time-node1.last_load_updated_time)
        if updated_load > 0 :
            node1.last_load_updated_time= self.time
            updated_load=updated_load
        else: 
            updated_load=0
        node1.load=updated_load
            
        updated_load= node2.load - (self.time-node2.last_load_updated_time)
        if updated_load > 0 :
            node2.last_load_updated_time= self.time
            updated_load=updated_load
        else: 
            updated_load=0
        node2.load=updated_load
            
        
        if node1.load<node2.load:
            return 1
        elif node1.load>node2.load:
            return -1
        else:
            return 0
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
       
        # Write your code ]here
        treasure.set_remaining_size() #for initialising remaining size
        self.time=treasure.arrival_time
        
        crewmate=self.crew_load.extract() 
        if not crewmate.had_treasure:
            self.crewmates_had_treasure.append(crewmate)
            # crewmate.old_treasure_updated_time= treasure.arrival_time# added later later
            # crewmate.old_time=crewmate.old_treasure_updated_time# added later later
            crewmate.had_treasure=True
        
        crewmate.treasure_array.append(treasure)
        # time=self.time #later added
        # crewmate.treasure.insert_new(treasure,time) #later added insert new
        updated_load= crewmate.load - (self.time-crewmate.last_load_updated_time)
        if updated_load > 0 :
            crewmate.last_load_updated_time= self.time
            updated_load=updated_load
        else: 
            updated_load=0
        crewmate.load=updated_load
        crewmate.load= crewmate.load+ treasure.size
        crewmate.last_load_updated_time=self.time
        self.crew_load.insert(crewmate)
        # for i in range(3):
        #     print(self.crew_load._data[i].load)
        
        
    
    def get_completion_time(self):
        '''7
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        #iterate over crewmates, iterate over treasure - crewmate me treasure heap- comparator, crew-heap me treasure extract kiyaa uska remaining size update kiyaa
        # Write your code here
        answer_array=[]
        for crewmate in self.crewmates_had_treasure:
            # crewmate=self.crewmates_had_treasure.pop()
            for treasure in crewmate.treasure_array:
                high_priority_treasure = self.function(treasure,crewmate,answer_array)
                if high_priority_treasure is None:
                    crewmate.treasure.insert_new(treasure,treasure.arrival_time)#time
                else:
                    crewmate.treasure.insert_new(treasure,treasure.arrival_time)#time
                    crewmate.treasure.insert_new(high_priority_treasure,treasure.arrival_time)#time para
                # crewmate.treasure.insert_new(treasure,treasure.arrival_time)#time
                crewmate.old_treasure_updated_time= treasure.arrival_time
                
           #CONFIRM TIME COMPLEXITY     
            while len(crewmate.treasure): 
                treasures=crewmate.treasure.extract_new(crewmate.old_treasure_updated_time)
                treasures.completion_time= crewmate.old_treasure_updated_time + treasures.remaining_size
                crewmate.old_treasure_updated_time= treasures.completion_time
                answer_array.append(treasures)
        # for crewmate in self.crewmates_had_treasure:
        #     if len(crewmate.treasure)!=0: 
        #         treasure_max= Treasure(-1,0,10000000000000000000000000)    
        #         self.function(treasure_max,crewmate, answer_array)   
                
        for crewmates in self.crewmates_had_treasure:
            crewmates.old_treasure_updated_time=0
            
        
            # crewmates.old_treasure_updated_time=crewmates.old_time
            for treasure in crewmates.treasure_array:
                treasure.set_remaining_size()
                #treasure.remaining_size=treasure.size
        answer_array.sort(key=lambda treasure: treasure.id)
        return answer_array
        pass
    
    def function(self,treasure,crewmate,answer_array):
        # if crewmate.treasure.top() is None:
        #     return None
        if len(crewmate.treasure)==0:
            return None
        high_priority_treasure=crewmate.treasure.extract_new(treasure.arrival_time) #time parameter
        old_remaining_size=high_priority_treasure.remaining_size
        high_priority_treasure.remaining_size=high_priority_treasure.remaining_size - (treasure.arrival_time-crewmate.old_treasure_updated_time)
        if high_priority_treasure.remaining_size <=0:
            high_priority_treasure.completion_time= old_remaining_size+crewmate.old_treasure_updated_time
            high_priority_treasure.remaining_size =0
            answer_array.append(high_priority_treasure)
            crewmate.old_treasure_updated_time = crewmate.old_treasure_updated_time + old_remaining_size
            return self.function(treasure,crewmate,answer_array)
        else:
            crewmate.old_treasure_updated_time= treasure.arrival_time
            # crewmate.treasure.insert_new(high_priority_treasure,treasure.arrival_time)
            return high_priority_treasure
            
            
        
        
    
    
    
    
    
    # You can add more methods if required
# strawhat=StrawHatTreasury(3)
# t1=treasure.Treasure(1,8,1)
# t2=treasure.Treasure(2,7,2)
# t3=treasure.Treasure(3,4,4)
# t4=treasure.Treasure(4,1,5)
# strawhat.add_treasure(t1)
# strawhat.add_treasure(t2)
# strawhat.add_treasure(t3)
# strawhat.add_treasure(t4)
# for i in range(3):
#     print(strawhat.crew_load._data[i].treasure_array)
# print(strawhat.crew_load._data[0].treasure_array[0].id)
# print(strawhat.crew_load._data[1].treasure_array[0].id)
# print(strawhat.crew_load._data[2].treasure_array[0].id,strawhat.crew_load._data[2].treasure_array[1].id)
#ans (2)(1)(3 4)
# print(strawhat.get_completion_time())

# strawhat=StrawHatTreasury(3)
# t1=treasure.Treasure(1,8,1)
# t2=treasure.Treasure(2,4,2)
# t3=treasure.Treasure(3,4,4)
# t4=treasure.Treasure(4,1,5)
# strawhat.add_treasure(t1)
# strawhat.add_treasure(t2)
# strawhat.add_treasure(t3)
# strawhat.add_treasure(t4)
# print(strawhat.crew_load._data[0].treasure_array[0].id,strawhat.crew_load._data[0].treasure_array[1].id)
# print(strawhat.crew_load._data[1].treasure_array[0].id)
# print(strawhat.crew_load._data[2].treasure_array[0].id)
# #ans (2 4),(1),(3)

# strawhat=StrawHatTreasury(2)
# t1=treasure.Treasure(1,8,1)
# t2=treasure.Treasure(2,7,2)
# t3=treasure.Treasure(3,4,4)
# t4=treasure.Treasure(4,1,5)
# strawhat.add_treasure(t1)
# strawhat.add_treasure(t2)
# strawhat.add_treasure(t3)
# strawhat.add_treasure(t4)
# print(strawhat.crew_load.heap[0].treasure_array[0].id,strawhat.crew_load.heap[0].treasure_array[1].id)
# print(strawhat.crew_load.heap[1].treasure_array[0].id,strawhat.crew_load.heap[1].treasure_array[1].id)
# #ans (2 4),(1 3)

# strawhat=StrawHatTreasury(2)
# t1=treasure.Treasure(1,8,1)
# t2=treasure.Treasure(2,7,2)
# t3=treasure.Treasure(3,4,4)
# t4=treasure.Treasure(4,1,5)
# t5=treasure.Treasure(5,7,6)
# t6=treasure.Treasure(6,12,7)
# t7=treasure.Treasure(7,4,8)
# t8=treasure.Treasure(8,6,9)
# t9=treasure.Treasure(9,3,10)
# strawhat.add_treasure(t1)
# strawhat.add_treasure(t2)
# strawhat.add_treasure(t3)
# strawhat.add_treasure(t4)
# strawhat.add_treasure(t5)
# strawhat.add_treasure(t6)
# strawhat.add_treasure(t7)
# strawhat.add_treasure(t8)
# strawhat.add_treasure(t9)
# print(strawhat.crew_load._data[0].treasure_array[0].id,strawhat.crew_load._data[0].treasure_array[1].id,strawhat.crew_load._data[0].treasure_array[2].id,strawhat.crew_load._data[0].treasure_array[3].id,strawhat.crew_load._data[0].treasure_array[4].id)
# print(strawhat.crew_load._data[1].treasure_array[0].id,strawhat.crew_load._data[1].treasure_array[1].id,strawhat.crew_load._data[1].treasure_array[2].id,strawhat.crew_load._data[1].treasure_array[3].id)
#ans (2 4 5 7 8),(1 3 6 9)


# strawhat=StrawHatTreasury(5)
# t1=treasure.Treasure(1,8,1)
# t2=treasure.Treasure(2,7,2)
# t3=treasure.Treasure(3,4,4)
# t4=treasure.Treasure(4,1,5)
# t5=treasure.Treasure(5,7,6)
# t6=treasure.Treasure(6,12,7)
# t7=treasure.Treasure(7,4,8)
# t8=treasure.Treasure(8,6,9)
# t9=treasure.Treasure(9,3,10)
# t10=treasure.Treasure(10,8,11)
# t11=treasure.Treasure(11,7,12)
# strawhat.add_treasure(t1)
# strawhat.add_treasure(t2)
# strawhat.add_treasure(t3)
# strawhat.add_treasure(t4)
# strawhat.add_treasure(t5)
# strawhat.add_treasure(t6)
# strawhat.add_treasure(t7)
# strawhat.add_treasure(t8)
# strawhat.add_treasure(t9)
# strawhat.add_treasure(t10)
# strawhat.add_treasure(t11)
# # print(strawhat.crew__data.heap[0].treasure_array[0].id,strawhat.crew_heap.heap[0].treasure_array[1].id,strawhat.crew_heap.heap[0].treasure_array[2].id,strawhat.crew_heap.heap[0].treasure_array[3].id,strawhat.crew_heap.heap[0].treasure_array[4].id)
# # print(strawhat.crew_heap.heap[1].treasure_array[0].id,strawhat.crew_heap.heap[1].treasure_array[1].id,strawhat.crew_heap.heap[1].treasure_array[2].id,strawhat.crew_heap.heap[1].treasure_array[3].id)
# for i in range(5):
#     #print ids
#     print(strawhat.crew_heap.heap[i].treasure_array)

# print(strawhat.crew_heap.heap[0].treasure_array[0].id)
# print(strawhat.crew_heap.heap[1].treasure_array[0].id,strawhat.crew_heap.heap[1].treasure_array[1].id)
# print(strawhat.crew_heap.heap[2].treasure_array[0].id,strawhat.crew_heap.heap[2].treasure_array[1].id,strawhat.crew_heap.heap[2].treasure_array[2].id)
# print(strawhat.crew_heap.heap[3].treasure_array[0].id,strawhat.crew_heap.heap[3].treasure_array[1].id)
# print(strawhat.crew_heap.heap[4].treasure_array[0].id,strawhat.crew_heap.heap[4].treasure_array[1].id,strawhat.crew_heap.heap[4].treasure_array[2].id)
# #ans (3 7 10),(4 6),(2 9 11),(1 8),(5)


# strawhat=StrawHatTreasury(5)
# t1=treasure.Treasure(1,8,1)
# t2=treasure.Treasure(2,7,2)
# t3=treasure.Treasure(3,4,4)
# t4=treasure.Treasure(4,1,5)
# t5=treasure.Treasure(5,7,6)
# t6=treasure.Treasure(6,12,7)
# t7=treasure.Treasure(7,4,8)
# t8=treasure.Treasure(8,6,9)
# t9=treasure.Treasure(9,3,10)
# t10=treasure.Treasure(10,8,11)
# t11=treasure.Treasure(11,7,12)
# t12=treasure.Treasure(12,4,13)
# strawhat.add_treasure(t1)
# strawhat.add_treasure(t2)
# strawhat.add_treasure(t3)
# strawhat.add_treasure(t4)
# strawhat.add_treasure(t5)
# strawhat.add_treasure(t6)
# strawhat.add_treasure(t7)
# strawhat.add_treasure(t8)
# strawhat.add_treasure(t9)
# strawhat.add_treasure(t10)
# strawhat.add_treasure(t11)
# strawhat.add_treasure(t12)
# # ans (3 7 10),(4 6),(2 9 11),(1 8),(5 12)