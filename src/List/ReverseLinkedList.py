__author__ = 'mingchen'

from ListBasics import ListNode

# @param {ListNode} head
# @return {ListNode}
def reverseList(head):
    if not head:
        return None
    next = head.next
    head.next = None
    return reverse(head, next)

def reverse(head, next):
    if not next:
        return head
    n = next.next
    next.next = head
    return reverse(next, n)

if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)

    a.printNodes()

    ra = reverseList(a)
    ra.printNodes()
