from linked_list import Linked_list


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - recursively divide the linked list into sub lists containing a single node
    - Repeatedly merge the sub lists to produce sorted sub lists until one remains

    Returns a sorted linked list
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """ Divide the unsorted list at midpoint into sublist
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = Linked_list()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    merges two linked lists, sorting by data in node
    returns a new, merged list
    """

    # create a new linked list that contains nodes
    # from merging left and right
    merged = Linked_list()

    # add a fake head to the empty linked list
    merged.add(0)

    # set current as head of the linked_list
    current = merged.head

    # obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # iterate over left and right until
    # we reach the tail node of either
    while left_head or right_head:
        # if the head node of left is None, we're past the tail
        # add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to set the loop condition to false
            right_head = right_head.next_node
        # if the head node of right is none, we're past the tail
        # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # call next on the left to set the loop condition to false
            left_head = left_head.next_node
        else:
            # not at either tail node
            # obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # if data on the left ois less that right,
            # set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # move left head to next node
                left_head = left_head.next_node
            # if data on left is greater that right set current to left node
            else:
                current.next_node = right_head
                # move right head to next node
                right_head = right_head.next_node
        # move current to next node
        current = current.next_node

    # discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

def verify(linked_list):
    # satisfy the condition for a linked list
    # of one node or and empty linked list by returning True
    n = linked_list.size()
    if n == 0 or n == 1:
        return True
    # a continue to the next node if next node is not None
    while linked_list.head.next_node:
        # if the current node is less tha the current node's next node then you
        # move the next node to the current node and continue
        if linked_list.head.data < linked_list.head.next_node.data:
            linked_list.head = linked_list.head.next_node 
        else:
            return False
    return True

l = Linked_list()
l.add(10)
l.add(44)
l.add(15)
l.add(34)
l.add(55)
l.add(200)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
print(verify(sorted_linked_list))
print(verify(l))















