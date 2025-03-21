class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_key(self, new_key):
        self.key = new_key

    def set_value(self, new_value):
        self.value = new_value
    
    def set_left(self, new_left):
        self.left = new_left

    def set_right(self, new_right):
        self.right = new_right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        value = self._find_recursively(key, self.root)
        return value

    def _find_recursively(self, key, current_node):
        value = None
        if current_node == None:
            print(f"Key {key} not found")
            return

        elif key == current_node.get_key():
            value = current_node.get_value()
        
        elif key < current_node.get_key():
            value = self._find_recursively(key, current_node.get_left())

        elif key > current_node.get_key():
            value = self._find_recursively(key, current_node.get_right()) 

        return value


    def insert(self, key, value=""):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self._insert_recursively(key, value, self.root)

    def _insert_recursively(self, key, value, current_node):
        update_node = current_node
        if current_node == None:
            new_node = TreeNode(key, value)
            update_node = new_node
        
        elif key == current_node.get_key():
            return
        
        elif key < current_node.get_key():
            current_node.set_left(self._insert_recursively(key, value, current_node.get_left()))

        else:
            current_node.set_right(self._insert_recursively(key, value, current_node.get_right()))

        return update_node

    def delete(self, key):
        self.root = self._delete_recursively(key, self.root)

    def _delete_recursively(self, key, current_node):
        if current_node == None:
            updated_node = None
        
        elif key == current_node.get_key():
            updated_node = self._remove_and_replace(current_node)
            return updated_node

        elif key < current_node.get_key():
            current_node.set_left(self._delete_recursively(key, current_node.get_left()))
            updated_node = current_node

        elif key > current_node.get_key():
            current_node.set_right(self._delete_recursively(key, current_node.get_right()))
            updated_node = current_node

        return updated_node

    def _remove_and_replace(self, node_to_del):
        if node_to_del.get_left() == None and node_to_del.get_right() == None:
            updated_node = None

        elif node_to_del.get_left() != None and node_to_del.get_right() == None:
            updated_node = node_to_del.get_left()

        elif node_to_del.get_left() == None and node_to_del.get_right() != None:
            updated_node = node_to_del.get_right()

        else:
            successor = self._find_successor(node_to_del.get_right())
            node_to_del.set_key(successor.get_key())
            node_to_del.set_value(successor.get_value())
            node_to_del.set_right(self._delete_recursively(successor.get_key(), node_to_del.get_right()))
        
            updated_node = node_to_del

        return updated_node
    
    def _find_successor(self, current_node):
        successor = current_node

        if current_node.get_left() == None:
            successor = self._find_successor(current_node.get_left())
            if successor == current_node.get_left():
                current_node.set_left(successor.get_right())

        return successor

    def min(self):
        current_node = self.root
        while current_node.get_left() != None:
            current_node = current_node.get_left()
        min_key = current_node.get_key()
        value = current_node.get_value()

        return min_key, value
    
    def max(self):
        current_node = self.root
        while current_node.get_right() != None:
            current_node = current_node.get_right()
        max_key = current_node.get_key()
        value = current_node.get_value()

        return max_key, value
    
    def height(self):
        return self._height_rec(self.root)
    
    def _height_rec(self, current_node):
        if current_node == None:
            height = 0
        else:
            left_height = self._height_rec(current_node.get_left())
            right_height = self._height_rec(current_node.get_right())
        
            height = max(left_height, right_height) + 1

        return height

    def balance(self):
        if self.root == None:
            return "100%"

        left_height = self._height_rec(self.root.get_left())
        right_height = self._height_rec(self.root.get_right())
        
        return f"{self._balance_score(left_height, right_height):.2f}%" 

    def _balance_score(self, x, y):
        if max(x, y) > 0:
            return (1 - abs(x - y) / max(x, y)) * 100
        else:
            return 100
    
    def transverse_inorder(self):
        if self.root != None:
            self._inorder(self.root)
            print()
        else:
            print("The binary tree is empty!")

    def _inorder(self, current_node: TreeNode):
        if current_node != None:
            self._inorder(current_node.get_left())
            print(f"{current_node.get_value()}({current_node.get_key()})", end=" ")
            self._inorder(current_node.get_right())

    def transverse_preorder(self):
        if self.root != None:
            self._preorder(self.root)
            print()
        else:
            print("The binary tree is empty!")

    def _preorder(self, current_node: TreeNode):
        if current_node != None:
            print(f"{current_node.get_value()}({current_node.get_key()})", end=" ")
            self._preorder(current_node.get_left())
            self._preorder(current_node.get_right())

    def transverse_postorder(self):
        if self.root != None:
            self._preorder(self.root)
            print()
        else:
            print("The binary tree is empty!")

    def _postorder(self, current_node: TreeNode):
        if current_node != None:
            self._postorder(current_node.get_left())
            self._postorder(current_node.get_right())
            print(f"{current_node.get_value()}({current_node.get_key()})", end=" ")

if __name__ == "__main__":
    test = BinarySearchTree()
    test.insert(2, "Acey")
    test.insert(1, "Disse")
    test.insert(3, "Aris")
    
    test.transverse_preorder()
    test.transverse_inorder()
    test.transverse_postorder()
    print(test.balance())

