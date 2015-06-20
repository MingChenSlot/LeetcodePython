__author__ = 'mingchen'

from ListBasics import ListNode
from ListBasics import constructLinkList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return None
        start = head
        prev = head
        head = head.next
        while head:
            if head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return start

    def deleteDuplicatesII(self, head):
        if not head:
            return None

        # cache includes all the duplicate ints
        cache = set()
        curr = head
        while curr.next:
            next = curr.next
            if curr.val == next.val:
                cache.add(curr)
                cache.add(next)
            curr = curr.next

        # test if start with duplicate numbers, determine head for new list
        start = head
        while head in cache:
            head = head.next
            start = head

        if not start:
            return None

        # once find head, continue
        prev = start
        head = head.next
        while head:
            if head in cache:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return start


if __name__ == "__main__":
    s = Solution()
    # a = constructLinkList([-1, -1, -2])
    # a.printNodes()
    # s.deleteDuplicates(a).printNodes()
    # b = constructLinkList([1, 1, 2, 3, 3])
    # s.deleteDuplicates(b).printNodes()
    # print s.deleteDuplicates(None)

    d = constructLinkList([-50,-50,-49,-48,-47,-47,-47,-46,-45,-43,-42,-41,-40,-40,-40,-40,-40,-40,-39,-38,-38,-38,-38,-37,-36,-35,-34,-34,-34,-33,-32,-31,-30,-28,-27,-26,-26,-26,-25,-25,-24,-24,-24,-22,-22,-21,-21,-21,-21,-21,-20,-19,-18,-18,-18,-17,-17,-17,-17,-17,-16,-16,-15,-14,-14,-14,-13,-13,-12,-12,-10,-10,-9,-8,-8,-7,-7,-6,-5,-4,-4,-4,-3,-1,1,2,2,3,4,5,6,6,7,8,8,9,9,10,10,10,11,11,12,12,13,13,13,14,14,14,15,16,17,17,18,20,21,22,22,22,23,23,25,26,28,29,29,29,30,31,31,32,33,34,34,34,36,36,37,37,38,38,38,39,40,40,40,41,42,42,43,43,44,44,45,45,45,46,47,47,47,47,48,49,49,49,50])
    # s.deleteDuplicates(d).printNodes()
    print "----------------------------------"
    a = constructLinkList([-1, -1, -2])
    b = constructLinkList([1, 1, 2, 3, 3])
    s.deleteDuplicatesII(a).printNodes()
    s.deleteDuplicatesII(b).printNodes()
    s.deleteDuplicatesII(d).printNodes()


