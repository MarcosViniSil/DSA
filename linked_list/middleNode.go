package main

func middleNode(head *ListNode) *ListNode {
    fast := head

	for fast.Next != nil{
		fast = fast.Next.Next
		head = head.Next
	}

	return head
}