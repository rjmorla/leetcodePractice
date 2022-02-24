def reverseLinkedList(head):
    if head is None or head.next is None:
        return head
    newhead = reverseLinkedList(head.next)
    head.next.next = head #sets head of next to point to itself to reverse
    head.next = None

    return newHead
    
    