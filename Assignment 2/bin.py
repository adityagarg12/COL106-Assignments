from avl import AVLTree
def obj_comp(object_1, object_2):
    if object_1._object_id < object_2._object_id:
        return -1
    elif object_1._object_id >object_2._object_id:
        return 1
    else:
        return 0
class Bin:
    def __init__(self, bin_id, capacity):
        # self._bin_data=[]
        self._bin_id= bin_id
        self._capacity= capacity
        self._remaining_capacity= capacity
        self.bin_data_tree= AVLTree(obj_comp)
    # def __eq__(self, other):
    #     return (self._capacity == other.capacity and 
    #             self._bin_id == other._bin_id)

    # def __lt__(self, other):
    #     if self._capacity != other.capacity:
    #         return self._capacity < other.capacity
    #     else:
    #         return self._bin_id > other._bin_id

    def add_object(self, object):
        # Implement logic to add an object to this bin
        self.insert(object.object_id,object)

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        self.delete(object_id)
