# Reverse a single linked list in place with O(N) time complexity 

# sll is single linked list
def reversesll(sll):
    if sll.head is None:
        return 
    
    curr_node = sll.head 
    previous_node, next_node = None, None 

    while curr_node is not None:
        next_node = curr_node.next_node 
        curr_node.next_node = previous_node
        previous_node = curr_node
        curr_node = next_node
    sll.head = previous_node