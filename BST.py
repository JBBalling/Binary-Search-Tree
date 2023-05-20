"""
(recursive) Binary Search Tree (BST)

a valid BST is a BST, where:
   - left is always smaller than the current nodes value
   - right is always greater or equal to the current nodes value 

            10
          /    \
         5      15
        / \    /  \ 
       2   5  13   22
"""
import sys
from typing import List, Optional, Union


class BST:
    def __init__(self, value: int, left: Optional[Union["BST", int]] = None, \
            right: Optional[Union["BST", int]] = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    # O(n) time | O(n) space
    def insert(self, value: int) -> None:
        current_node = self
        while True:
            if current_node.value <= value:
                # go to the right
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = BST(value)
                    break
            else:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = BST(value)
                    break
        
        # return self

    # O(n) time | O(n) space
    def contains(self, value: int) -> None:
        current_node = self
        if current_node.value < value:
            if current_node.right is not None:
                # right
                return current_node.right.contains(value)
        elif current_node.value > value:
            if current_node.left is not None:
                return current_node.left.contains(value)
        else:
            return True

        return False

    def validate(self) -> bool:
        stack = [(-sys.maxsize-1, self, sys.maxsize)]
        while stack:
            (min, current, max) = stack.pop()
            if current.value < min or current.value >= max:
                return False
            if current.left is not None:
                stack.append((min, current.left, current.value))
            if current.right is not None:
                stack.append((current.value, current.right, max))

        return True

    # O(n) time | O(n) space
    def remove(self, value) -> None:
        if not self:
            return self

        if self.value > value:
            # go left
            if self.left:
                self.left = self.left.remove(value)
        elif self.value < value:
            if self.right:
                self.right = self.right.remove(value)
        else:
            # case 1: node which should be deleted is a leaf node
            if not self.left and not self.right:
                return None
            # case 2: node which should be deleted has only 1 child (left or right)
            elif not self.left:
                self.value = self.right.value
                self.right = self.right.right
                return self
            elif not self.right:
                self.value = self.left.value
                self.left = self.left.left
                return self
            # case 3: node which should be deleted has both children
            else:
                successor = self.right.inOrderSuccessor()
                self.value = successor.value
                self.right = self.right.remove(successor.value)

        return self

    def inOrderSuccessor(self):
        while self.left:
            self = self.left
        return self

# Depth-First-Search
def printInOrderTraversal(tree: BST) -> None:
    if tree:
        printInOrderTraversal(tree.left)
        print(tree.value)
        printInOrderTraversal(tree.right)


def inOrderTraversal(tree: BST, array: List) -> List:
    if tree:
        inOrderTraversal(tree.left, array)
        array.append(tree.value)
        inOrderTraversal(tree.right, array)

    return array

def preOrderTraversal(tree: BST, array: List) -> List:
    if tree:
        array.append(tree.value)
        preOrderTraversal(tree.left, array)
        preOrderTraversal(tree.right, array)
    
    return array


def postOrderTraversal(tree: BST, array: List) -> List:
    if tree:
        postOrderTraversal(tree.left, array)
        postOrderTraversal(tree.right, array)
        array.append(tree.value)

    return array


# Breadth First Search (BFS)
def BFS(tree: BST) -> List:
    queue = [tree]
    values = []
    while len(queue) != 0:
        tree = queue.pop(0)
        values.append(tree.value)
        if tree.left:
            queue.append(tree.left)
        
        if tree.right:
            queue.append(tree.right)

    return values


if __name__=="__main__":
    # init tree
    #        10
    #      /    \
    #     5      15
    #    / \    /  \ 
    #   2   5  13   22
    root = BST(10)
    root.left = BST(5)
    root.right = BST(15)
    root.left.left = BST(2)
    root.left.right = BST(5)
    root.right.left = BST(13)
    root.right.right = BST(22)
    # InOrderTraversal: 2, 5, 5, 10, 13, 15, 22
    # printInOrderTraversal(root)
    q = inOrderTraversal(root, [])
    print(f"inOrderTraversal: {q}")
    # PreOrderTraversal: 10, 5, 2, 5, 15, 13, 22
    q = preOrderTraversal(root, [])
    print(f"preOrderTraversal: {q}")
    # PostOrderTraversal: 2, 5, 5, 13, 22, 15, 10
    q = postOrderTraversal(root, [])
    print(f"postOrderTraversal: {q}")

    root.insert(21)
    root.insert(3)
    print(inOrderTraversal(root, []))
    root.insert(4)
    print(inOrderTraversal(root, []))
    root.remove(21)
    root.remove(3)
    root.remove(4)
    print(inOrderTraversal(root, []))
    
    print(root.contains(5))
    print(root.contains(43))
    print(root.validate())
    print(f"Breadth-First-Search: {BFS(root)}")
