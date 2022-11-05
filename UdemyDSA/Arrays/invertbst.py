# Given the root of a binary tree, invert the tree, and return its root.

# Inversion means  2       becomes    2 
#               1     3            3     1

import bst 

def invertBST(root):
    if root is None:
        return 
    
    temp = root.left_child
    root.left_child = root.right_child 
    root.right_child = temp 

    invertBST(root.left_child)
    invertBST(root.right_child)

    return root

if __name__ == '__main__':
    bst1 = bst.BinarySearchTree()
    bst1.insert(2)
    bst1.insert(1)
    bst1.insert(3)
    invertBST(bst1.root)