from node import Node

# def comp_
# 1(node_1, node_2):
#     if node_1._value != node_2._value :
#         return node_1._value-node_2._value
#     else:
#         return node_1._id - node_2._id

class AVLTree:
    def __init__(self, compare_function):
        self.root = None
        self.size = 0
        self.comparator = compare_function
    
    def _min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._min_value_node(node.left)

    def _height(self, node):
        if not node:
            return 0
        return node.height
    def _rotate_left(self, z):
        y = z.right
        x = y.left


        y.left = z
        z.right = x

        if x is not None:
            x._parent = z
        y._parent = z._parent
        z._parent = y

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        x = y.right

        y.right = z
        z.left = x

        if x is not None:
            x._parent = z
        y._parent = z._parent
        z._parent = y

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y
    def _balance_number(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _balance(self, node):
        balance = self._balance_number(node)

        if balance > 1:
            if self._balance_number(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_number(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    


    def insert(self, key, value=None):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        
        if self.comparator(value, node._value) < 0:
            node.left = self._insert(node.left, key, value)
            node.left._parent = node  
        elif self.comparator(value, node._value) > 0:
            node.right = self._insert(node.right, key, value)
            node.right._parent = node  
        else:
            node._value = value
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        return self._balance(node)

    def delete(self, value):
        if self.root is not None:
            self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node
        
        if self.comparator(value, node._value) < 0:
            node.left = self._delete(node.left, value)
            if node.left:
                node.left._parent = node 
        elif self.comparator(value, node._value) > 0:
            node.right = self._delete(node.right, value)
            if node.right:
                node.right._parent = node  
        else:
            if node.left is None:
                temp = node.right
                if temp is not None:
                    temp._parent = node._parent 
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                if temp is not None:
                    temp._parent = node._parent 
                node = None
                return temp
            
            temp = self._min_value_node(node.right)
            
            node._key = temp._key
            node._value = temp._value
            
            node.right = self._delete(node.right, temp._value)
            if node.right:
                node.right._parent = node  
        
        if node is None:
            return node
        
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        
        return self._balance(node)
    
    # def delete(self, value):
    #     self.root, deleted_node = self._delete(self.root, value)
    #     return deleted_node

    # def _delete(self, node, value):
    #     if not node:
    #         return node, None

    #     if self.comparator(value, node._value) < 0:
    #         node.left, deleted_node = self._delete(node.left, value)
    #     elif self.comparator(value, node._value) > 0:
    #         node.right, deleted_node = self._delete(node.right, value)
    #     else:
    #         # Node to be deleted found
    #         deleted_node = node
    #         if not node.left:
    #             return node.right, deleted_node
    #         elif not node.right:
    #             return node.left, deleted_node

    #         temp = self._min_value_node(node.right)
    #         node._key = temp._key
    #         node._value = temp._value
    #         node.right, _ = self._delete(node.right, temp._value)

    #     node.height = 1 + max(self._height(node.left), self._height(node.right))
    #     return self._balance(node), deleted_node

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if not node:
            return None
        if key < node._key:
            return self._find(node.left, key)
        elif key > node._key:
            return self._find(node.right, key)
        else:
            return node


    # def find_best_fit_bin(self, node, object_size, object_color):
        

    #     if object_color ==1:
    #         if not node:
    #             return None
    #         if node.value < object_size:
    #             return self.find_best_fit_bin(node.right, object_size, object_color) 
    
    #         left_fit = self.find_best_fit_bin(node.left, object_size, object_color)
    #         if left_fit:
    #             return left_fit

    #         return node
        
    #     if object_color==2:
    #         if not node:
    #             return None
    #         if node.value < object_size:
    #             return self.find_best_fit_bin(node.right, object_size, object_color) 
            
    #         if node.value== object_size and node.value==node.right.value:
    #             return self.find_best_fit_bin(node.right, object_size, object_color)
    #         if node.value >object_size:
    #             if node.value == node.left.value and node.id> node.left.id:
    #                 temp = node
    #             left_fit = self.find_best_fit_bin(node.left, object_size, object_color)
    