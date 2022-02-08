# Trees

A tree is a type of graph with the next characteristics

- It has a root Node
- Every node has child nodes
- The structure is directed
- No have cycles


## Ternary Tree

Can have three children

## Time complexity

- **Storing:**  O(N) Time and Space
- **Traverse:** O(N) Time O(1) Space

## Balance

A binary three whose nodes all have left and right subtrees whose heights differ by no more than 1

![Balanced](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7f752bfd-949f-4c27-bb6b-6f1d1d20fc1d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220208T020003Z&X-Amz-Expires=86400&X-Amz-Signature=e504a36d5927f584bc3231577f4e1ae8992f23f7077e5285db40015c597e5023&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

## Binary Tree

It has at most two children nodes.

A binary tree **node** consists of the following components:

- Data
- Pointer to Left Child
- Pointer to Right Child

Below are some key terminologies related to a binary tree.

- **Node** – The most elementary unit of a binary tree.
- **Root** – The root of a binary is the topmost element. There is only one root in a binary tree.
- **Leaf** – The leaves of a binary tree are the nodes which have no children.
- **Level** – The level is the generation of the respective node. The root has level 0, the children of the root node is at level 1, the grandchildren of the root node is at level 2 and so on.
- **Parent** – The parent of a node is the node that is one level upward of the node.
- **Child** – The children of a node are the nodes that are one level downward of the node.


## Perfect binary tree

All nodes have two child-nodes and whose leaf nodes all have the same depth.

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7895b772-cd55-4ea2-aed7-4b9d1821cdc7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220208T020137Z&X-Amz-Expires=86400&X-Amz-Signature=e51dbfc522645dae22862f8e7b0b161046769932666563c949c637403ed6e0a2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

## Complete binary tree

Every level, except possibly the last, is completly filled , and all the nodes in the last level are as fart left as possible.

![](https://static.javatpoint.com/ds/images/full-binary-tree-vs-complete-binary-tree.png)

## Full binary tree

A binary tree whose nodes all have either two children nodes or zero child nodes.
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/720ecd32-2f65-4ad6-bf4d-cc5f73c201a2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220208T020326Z&X-Amz-Expires=86400&X-Amz-Signature=e72535ba72ee4fc4b00cd026f5aae8bba26f51cffa4eb235d51add696ff34b71&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)


## Binary Tree Traversal

Process of visiting (checking / updating) each node in a tree data structure,exactly once.

Unlike linked lists, one dimensional arrays, etc., which are canonically traversed in linear order, trees may be traversed in multiple ways, They may be traversed in depth-first or breadth-first order.

### Depth-first traversal

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Sorted_binary_tree_ALL_RGB.svg/293px-Sorted_binary_tree_ALL_RGB.svg.png)

#### In-Order traversal


Means to "visit" the left branch, then the current node, and finally, the right branch.

- Check if the current node is empty / null.

- Traverse the left subtree by recursively calling the in-order function.

- Display the data part of the root (or current node).

- Traverse the right subtree by recursively calling the in-order function.

[A, B, C, D, E, F, G, H, I]

```python

def inOrderTraversal(node):
    if node:
        inOrderTraversal(node.left)
        visit(node)
        inOrderTraversal(node.right)
```

#### Pre-Order traversal

Visits the current node before its child nodes

- Check if the current node is empty / null.

- Display the data part of the root (or current node).

- Traverse the left subtree by recursively calling the pre-order function.

- Traverse the right subtree by recursively calling the pre-order function.

[F, B, A, D, C, E, G, I, H]

```python

def preOrderTraversal(node):
    if node:
        visit(node)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)
```

#### Post-Order traversal

Visits the current node after its child nodes.

- Check if the current node is empty / null.

- Traverse the left subtree by recursively calling the post-order function.

- Traverse the right subtree by recursively calling the post-order function.

- Display the data part of the root (or current node).

[A, C, E, D, B, H, I, G, F]

```python

def postOrderTraversal(node):
    if node:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        visit(node)
```