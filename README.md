# Data Structures

### Implement a Stack - with tests

This stack was created by composition; composed of the Linked-List that already contains all the functionality that the stack needs. This makes sense since the stack is essentially a subset of a Linked List.

##### Big O Notation
The stack contains 3 main functions - push, pop and length.

- `__len__()` is "O(1)" -- The size of the stack is incremented or decremented each time a node is pushed or popped. This gives us direct access to that size variable in constant time. No looping required.
- `push()` is "O(1)" -- You create a node and point to the next one. No looping required.
- `pop()` is "O(1)" -- You remove a node and the pointer to it. It's constant time -- You remove a node and the pointer to it. It's constant time.



