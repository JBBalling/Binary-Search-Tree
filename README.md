# Binary Search Tree (BST)


            10
          /    \
         5      15
        / \    /  \ 
       2   5  13   22

## Methods

### insert 

- insert a node into the tree
- avg. case O(log n)

### search

- searching for a value inside the tree
- avg. case O(log n)

### delete

- searching for a value inside the tree, remove it and update the tree
- avg. case O(log n)

### validate

- validates the tree, that it is a valid Binary Search Tree:
- a **valid, ordered or sorted BST** is a tree-like data structure with the key of its internal node is greater than the keys in the respective nodes's left subtree and less than the ones in the right subtree.   

## Functions

### In-Order-Traversal

- traverse the tree from left subtree then right subtree
- Example: [2, 5, 5, 10, 13, 15, 22]

### Pre-Order Traversal

- traverse the tree starting from the root, followed by left and right subtrees
- Example: [10, 5, 2, 5, 15, 13, 22]

### Post-Order Traversal

- traverse the tree starting from left subtree, then right subtree and finally visit the root node
- Example: [2, 5, 5, 13, 22, 15, 10]

### Breadth-First-Search (BFS)

- traverse the tree in Breadth First Search manner by visiting the nodes from top to bottom and from left to right
- Example: [10, 5, 15, 2, 5, 13, 22]

## Applications:

- Sorting
- Priority Queues