from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

def obmap_comp(ob1,ob2):
    if ob1._object_id<ob2._object_id:
        return -1
    elif ob1._object_id>ob2._object_id:
        return 1
    else: return 0
def obj_comp(object_1, object_2):
    if object_1._object_id < object_2._object_id:
        return -1
    elif object_1._object_id >object_2._object_id:
        return 1
    else: 
        return 0

def bin_capacity_comp(bin1,bin2):
    if bin1._capacity < bin2._capacity:
        return -1
    elif bin1._capacity > bin2._capacity:
        return 1
    else:
        if bin1._bin_id < bin2._bin_id:
            return -1
        elif bin1._bin_id > bin2._bin_id:
            return 1
        else:
            return 0

def bin_id_comp(bin1,bin2):
    if bin1._bin_id < bin2._bin_id:
        return -1
    elif bin1._bin_id > bin2._bin_id:
        return 1
    else:
        return 0
    

class GCMS:    
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bin_ids=   AVLTree(bin_id_comp)
        self.bin_capacity = AVLTree(bin_capacity_comp)
        self.obmaap = AVLTree(obmap_comp)
         

    def add_bin(self, bin_id, capacity):
        bin = Bin(bin_id,capacity)
        # self.bin_capacity.insert(bin._remaining_capacity,bin)
        self.bin_capacity.insert(bin._capacity,bin)
        self.bin_ids.insert(bin_id,bin)
        # print(self.bin_capacity.root._key)
        # print(self.bin_ids.root._key)
        return bin
    
    def blue(self,object):
        ans_bin = None
        
        node = self.bin_capacity.root
       
        while node:
            if node._key< object._size:
                node = node.right
            else:
                ans_bin= node
                node=node.left
        return ans_bin
    
    def yellow(self,object):
        # ans_bin=None
        # min= 1000000000
        # node = self.bin_capacity.root
        # while node:
        #     if node._key < object._size:
        #         node=node.right
        #     elif node._key > object._size:
        #         if node.left is not None and node.left._key != node._key:
        #             if node._key<= min:
        #                 ans_bin = node
        #             node = node.left
        #         else:
        #             if node._key<= min:
        #                 ans_bin=node
        #                 min = ans_bin._key
        #             node=node.right
        #     elif node._key > object._size and node.left_key == node._key:
        #         ans_bin=node
        #         min = ans_bin._key
        #         node= node.right   
        # return ans_bin
        ans_bin = None
        node = self.bin_capacity.root
        while node:
            if node._key< object._size:
                node= node.right
            else:
                ans_bin= node
                node=node.left
        if ans_bin:
            node = self.bin_capacity.root
            while node:
                if node._key == ans_bin._key:
                    ans_bin = node
                    node = node.right
                elif node._key<ans_bin._key:
                    node=node.right   
                else:
                    node = node.left
        return ans_bin             
    def green(self,object):
        ans_bin = None
        node = self.bin_capacity.root
        while node:
            ans_bin=node
            node = node.right
            # if node._key< object._size:
            #     node = node.right
            # else:
            #     ans_bin= node
            #     node=node.right
        if ans_bin._key < object._size:
            return None
        return ans_bin   
    
    def red(self,object):
        ans_bin = None
        node = self.bin_capacity.root
        while node:
            ans_bin = node
            node = node.right
        if ans_bin._key < object._size:
            ans_bin = None
        if ans_bin:
            node = self.bin_capacity.root
            while node:
                if node._key == ans_bin._key:
                    ans_bin = node
                    node = node.left   
                else:
                    node = node.right
        return ans_bin
         
        
        
        
         
    def add_object(self, object_id, size, color):
        object= Object(object_id,size,color)
        if color == Color.BLUE:
            ans_bin= self.blue(object)
            # print(ans_bin._key)
            if ans_bin is None:
                # print('ac')
                raise NoBinFoundException
            # self._inorder_traversal(self.bin_capacity.root)
            
            updated_node=ans_bin._value
            object.bin = updated_node
            updated_node_id=updated_node._bin_id
            updated_node_cap=updated_node._capacity
            # print(updated_node._capacity)
            self.bin_capacity.delete(updated_node) #node is not getting deleted
            # self.bin_ids.delete(updated_node)
            bin = self.bin_ids.find(updated_node_id)
            bin._value._capacity -=size
            # print('d')
            # print(self.bin_ids.root._value._bin_id)
            # print(updated_node._remaining_capacity)
            # self._inorder_traversal(self.bin_capacity.root)
            # updated_node._remaining_capacity-=size
            # self.bin_capacity.insert(updated_node._remaining_capacity,updated_node)
            # bin=self.add_bin(updated_node_id,updated_node_cap - size)
            self.bin_capacity.insert(updated_node_cap-size,Bin(updated_node_id,updated_node_cap-size))
            # print(self.bin_ids.root._value._capacity)
            # print(bin._capacity)
            # self._inorder_traversal(self.bin_capacity.root)
            # print('a')
            bin._value.bin_data_tree.insert(object_id,object)
            # print('b')
            # print(self.bin_capacity.root._key)
            self.obmaap.insert(object_id,object)
            # self._inorder_traversal(bin.bin_data_tree.root)

        if color==Color.YELLOW:
            ans_bin= self.yellow(object)
            if ans_bin is None:
                # print('ac')
                raise NoBinFoundException
            updated_node=ans_bin._value
            object.bin = updated_node
            updated_node_id=updated_node._bin_id
            updated_node_cap=updated_node._capacity
            # print(updated_node._capacity)
            self.bin_capacity.delete(updated_node) #node is not getting deleted
            # self.bin_ids.delete(updated_node)
            bin = self.bin_ids.find(updated_node_id)
            bin._value._capacity -=size
            # print('d')
            # print(self.bin_ids.root._value._bin_id)
            # print(updated_node._remaining_capacity)
            # self._inorder_traversal(self.bin_capacity.root)
            # updated_node._remaining_capacity-=size
            # self.bin_capacity.insert(updated_node._remaining_capacity,updated_node)
            # bin=self.add_bin(updated_node_id,updated_node_cap - size)
            self.bin_capacity.insert(updated_node_cap-size,Bin(updated_node_id,updated_node_cap-size))
            # print(self.bin_ids.root._value._capacity)
            # print(bin._capacity)
            # self._inorder_traversal(self.bin_capacity.root)
            # print('a')
            bin._value.bin_data_tree.insert(object_id,object)
            # print('b')
            # print(self.bin_capacity.root._key)
            self.obmaap.insert(object_id,object)
            # self._inorder_traversal(bin.bin_data_tree.root)
            
        if color==Color.GREEN:
            ans_bin= self.green(object)
            if ans_bin is None:
                # print('ac')
                raise NoBinFoundException
            updated_node=ans_bin._value
            object.bin = updated_node
            updated_node_id=updated_node._bin_id
            updated_node_cap=updated_node._capacity
            # print(updated_node._capacity)
            self.bin_capacity.delete(updated_node) #node is not getting deleted
            # self.bin_ids.delete(updated_node)
            bin = self.bin_ids.find(updated_node_id)
            bin._value._capacity -=size
            # print('d')
            # print(self.bin_ids.root._value._bin_id)
            # print(updated_node._remaining_capacity)
            # self._inorder_traversal(self.bin_capacity.root)
            # updated_node._remaining_capacity-=size
            # self.bin_capacity.insert(updated_node._remaining_capacity,updated_node)
            # bin=self.add_bin(updated_node_id,updated_node_cap - size)
            self.bin_capacity.insert(updated_node_cap-size,Bin(updated_node_id,updated_node_cap-size))
            # print(self.bin_ids.root._value._capacity)
            # print(bin._capacity)
            # self._inorder_traversal(self.bin_capacity.root)
            # print('a')
            bin._value.bin_data_tree.insert(object_id,object)
            # print('b')
            # print(self.bin_capacity.root._key)
            self.obmaap.insert(object_id,object)
            # self._inorder_traversal(bin.bin_data_tree.root)
               
        if color==Color.RED:
            ans_bin= self.red(object)
            if ans_bin is None:
                # print('ac')
                raise NoBinFoundException
            updated_node=ans_bin._value
            object.bin = updated_node
            updated_node_id=updated_node._bin_id
            updated_node_cap=updated_node._capacity
            # print(updated_node._capacity)
            self.bin_capacity.delete(updated_node) #node is not getting deleted
            # self.bin_ids.delete(updated_node)
            bin = self.bin_ids.find(updated_node_id)#removed _id
            bin._value._capacity -=size
            # print('d')
            # print(self.bin_ids.root._value._bin_id)
            # print(updated_node._remaining_capacity)
            # self._inorder_traversal(self.bin_capacity.root)
            # updated_node._remaining_capacity-=size
            # self.bin_capacity.insert(updated_node._remaining_capacity,updated_node)
            # bin=self.add_bin(updated_node_id,updated_node_cap - size)
            self.bin_capacity.insert(updated_node_cap-size,Bin(updated_node_id,updated_node_cap-size))
            # print(self.bin_ids.root._value._capacity)
            # print(bin._capacity)
            # self._inorder_traversal(self.bin_capacity.root)
            # print('a')
            bin._value.bin_data_tree.insert(object_id,object)
            # print('b')
            # print(self.bin_capacity.root._key)
            self.obmaap.insert(object_id,object)
            # self._inorder_traversal(bin.bin_data_tree.root)    
            
            
            
            
            
            
            
            
            
    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        node=self.obmaap.find(object_id)
        node2=node
        if node is None:
            return None
        bin_id= node._value.bin._bin_id
        bin_cap=node._value.bin._capacity
        
        bin = self.bin_ids.find(bin_id)
        a= bin._value.bin_data_tree.find(object_id)
        size= a._value._size
        color=a._value._color
        obin=a._value.bin
        object=Object(object_id,size,color,obin)
        bin._value._capacity+=size
        bin._value.bin_data_tree.delete(object)
        self.bin_capacity.delete(bin._value)
        self.bin_capacity.insert(bin_cap+size,Bin(bin_id,bin_cap+size))
        self.obmaap.delete(object)

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        ans=self.bin_ids.find(bin_id)
        if ans:
            bin = ans._value
            object_ids = []
            self._inorder_traversal(bin.bin_data_tree.root, object_ids)
            return (bin._capacity, object_ids)
        else:
            raise KeyError("Bin not found.")
    
    def _inorder_traversal(self, node, object_ids):
        if not node:
            return
        self._inorder_traversal(node.left, object_ids)
        object_ids.append(node._key)
        self._inorder_traversal(node.right, object_ids)
        
    # def _inorder_traversal(self, node):
    #     if not node:
    #         return
    #     self._inorder_traversal(node.left)
    #     print(node._key)
    #     self._inorder_traversal(node.right)
          
    def object_info(self, object_id):
        node=self.obmaap.find(object_id)
        node2=node
        if node is not None:
            bin_id= node._value.bin._bin_id
            return bin_id
        else:
            return None
    
    