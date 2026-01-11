
from .linked_list_definition import ListNode
from .linked_list_definition import Node

def seed(values:list[int]) -> ListNode:
    linked_list = ListNode()
    aux = linked_list
    
    for value in values:
        node = ListNode(value)
        aux.next = node
        aux = aux.next
    
    return linked_list.next


def seed_index(values:list[int],index:int) -> ListNode:
    linked_list = ListNode()
    aux = linked_list
    node_cycle = None
    last_node = None
    for i,value in enumerate(values):
        node = ListNode(value)
        
        if i == len(values) - 1:
            last_node = node
        if i == index:
            node_cycle = node 
        
        aux.next = node
        aux = aux.next

        if last_node:
            last_node.next = node_cycle

    return linked_list.next

def print_linked_list(head:ListNode) -> None:
    if not head:
        print("empty")
        return
    curr = head
    
    while curr:
        if not curr.next:
            print(curr.val,end=" ")
        else:
            print(curr.val,end=" -> ")
        
        curr = curr.next
    
    print()


