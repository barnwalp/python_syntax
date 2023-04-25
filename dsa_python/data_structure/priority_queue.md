### Priority Queue Introduction
1. **Priority Queue** is an abstract data type that operates similar to a normal queue except that each element has a certain priority. The priority of the elements in the priority queue determines the order in which elements are removed from the PQ.

2. **Priority queue** only supports comparable data, meaning the data inserted into the priority queue must be able to be ordered in some way either from least to greatest or greatest to least. This is so that we are able to assign relative priorities to each element.

poll() - remove the element that has highest priority in our PQ

### When and where is a PQ used?
- Used in certain implementation of Dijkistra's shortes path algo
- Anytime you need the dynamically fetch the next best or next worst element
- Used in Huffman coding (lossless data compression)
- Breath first search (BFS) algorithms to continuously grab the next most promising node.
- Used by minimum spanning tree (MST) algorithm

### Turning Min PQ into max PQ:
**Solution-1:** 
Let x, y be numbers in the PQ. For a min PQ, if x<=y then x comes out of the PQ before y, so the negation of this is if x>=y then y comes out before x. 

**Solution-2:** 
First negate the number as you insert them into the PQ and negate them again when they are taken out. This has the same effect as negating the comparator.

### Ways of implementing a Priority Queue
- Although priority queue can be implemented using data structure other than heap as it is an abstract data type (ADT), but heaps are commonly used as this gives best possible time complexity. 
- Apart from binary heap, we can also use **fibonacci heap**, **bimonial heap** and **pairing heap**.

### Priority Queue with binary heap
- A **binary heap** is a **binary tree** that supports the **heap invariant**. In a binary tree every node has at most two children.
- A **complete binary tree** is a tree in which at every level, except possibly the last is completely filled and all the nodes are as far left as possible.
- Binary heap can be representated simply as an array, whereas if i is the parent node index, **left child** index is at **2i+1** and **right child** index will be **2i+2** (zero based)

### Adding element in a binary heap
1. Add element to a in heap at it's lowest node in a way that it does not violate complete binary tree property.
2. Swap the newly added element with it's parent node (bubble-up) untill heap-invariant is satisfied.

### Removing elements from binary heap
