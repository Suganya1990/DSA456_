
import random 
import matplotlib.pyplot as plt
from collections import deque

# basic building block (node) for insertion, key holds value, left and right points to child nodes

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None   
        self.right = None

class BST: 
    
    def __init__(self):                                      #intialize with no nodes (root is empty)
        self.root = None
   
    def insert(self, key):                                  #insert key into the tree    
        self.root = self._insert(self.root, key)
  
    def _insert(self, node, key):                           #find the correct place for the new key to be inserted 
        if not node:                                        #exit out of recursive function by creating a new node if spot is empty
            return Node(key)
        if key > node.key:                                  #recursive call back until 
            node.right = self._insert(node.right, key)
        else: 
            node.left = self._insert(node.left, key)       
        return node                                         #returns the updated subtree
   
    def height(self, node=None):
        if node is None:                                       #when function is called with no arguments   
            node = self.root
        if node is None:                                        #when we hit a node in recursion
            return -1
        q = deque([(node, 0)])
        max_height = 0

        while q:
            current, depth = q.popleft()
            max_height = max(max_height, depth)
            if current.left:
                q.append((current.left, depth + 1))
            if current.right:
                q.append((current.right, depth + 1))
        return max_height
    
    def imbalance(self):                                        #Returns the imbalance of the tree
            return abs(self.subtree_height(self.root.left) - self.subtree_height(self.root.right))
    
    def subtree_height(self, node):                             #calculate height of any subtree
         if not node:
                return -1
         return 1 + max(self.subtree_height(node.left), self.subtree_height(node.right))
    
class AVLNode(Node):                                            #Basic Node Building Block 
     def __init__(self, key):
          super().__init__(key)
          self.height = 1

class AVLTree:   #AVL Tree 
    def __init__(self):
         self.root = None
         self.rotation = 0

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)

        else:
             node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_rotate_right(node)

        if balance > 1 and key < node.left.key:
            self.rotation+=1
            return self._rotate_right(node)
        
        if balance < -1 and key > node.right.key:
            self.rotations += 1
            return self._rotate_left(node)
        
        if balance > 1 and key > node.left.key:
             self.rotation+=2
             node.left = self._rotate_left(node.left)
             return self._rotate_right(node)
        
        if balance < -1 and key < node.right.key:
            self.rotation+=2
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

#GENERATE DATA AND RECORD METRICS
def main():
    heights = []
    imbalances = []
    permutations = []

    for _ in range(1000):                                       #runs & creates 1000 BST
        nums = random.sample(range(1, 21), 20)                  # To create a random permutation of the numbers 1 to 20
        tree = BST()                                            # Creates a new BST Object
        for num in nums:                                        #loops through every number in permutaiton 
            tree.insert(num)                                    # Inserts each into BST 
        heights.append(tree.height())                           # Calcs total height and appends to array
        imbalances.append(tree.imbalance())                     # Calcs diff in  height between left and right and appends to array
        permutations.append(nums)                               # Used to build this tree
   
   # Histogram of Heights
    plt.hist(heights, bins=range(min(heights), max(heights)+2), edgecolor='black')
    plt.title("Histogram of BST Heights (1000 Trees)")
    plt.xlabel("Height")
    plt.ylabel("Frequency")
    plt.savefig("height_histogram.png")
    plt.show()  

    # Histogram of Heights
    plt.hist(imbalances, bins=range(min(imbalances), max(imbalances)+2), edgecolor='black')
    plt.title('BST Imbalance Distribution (1000 Trees)')
    plt.xlabel('Imbalance (|left - right|)')
    plt.ylabel('Frequency')
    plt.savefig("imbalance_histogram.png")
    plt.show()

if __name__ == "__main__":
    main()