
from .linked_list_definition import ListNode

def seed(values:list[int]) -> ListNode:
    linked_list = ListNode()
    aux = linked_list
    
    for value in values:
        node = ListNode(value)
        aux.next = node
        aux = aux.next
    
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


