# data_structures

push O(1): adds a node to the head of the list
append O(1): adds a node to the tail of the list
pop O(1): removes and returns a node from the head
shift O(1): removes and returns a node from the tail
remove O(n): removes the first node found with the given value

helper functions:
list_begins O(1): used by push and append to add a node to a previously empty list
pop_single_node O(1): used by pop and shift to take out the only node in a list