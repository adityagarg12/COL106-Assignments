'''
    Python file to implement the class CrewMate
'''
from treasure import Treasure
from heap import Heap

def priority_comp(t1,t2,time):
    if t1.priority(time)>t2.priority(time):
        return 1
    elif t1.priority(time)<t2.priority(time):
        return -1
    else:
        if t1.id<t2.id:
            return 1
        elif t1.id>t2.id:
            return -1
        else:
            return 0
            
    
class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            N   ne
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.treasure_array=[]
        self.treasure= Heap(priority_comp,[])
        self.load=0
        self.last_load_updated_time=0
        self.had_treasure=False
        self.old_treasure_updated_time=0
        self.old_time=self.old_treasure_updated_time
        pass
    
    # Add more methods if required
    
    