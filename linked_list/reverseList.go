package main

type ListNode struct {
	    Val int
	    Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
    if head == nil{
        return nil
    }

	var newList *ListNode
	newList = nil

	for head != nil{
		nextNode := head.Next
		head.Next = newList
		newList = head
		head = nextNode
	}

	return newList
}


