__author__ = 'mingchen'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printNodes(self):
        node = self
        print "[",
        while node:
            print node.val,
            node = node.next
        print "]\n"

def constructLinkList(values):
    if len(values):
        start = ListNode(values[0])
        prev = start
        for i in range(1, len(values)):
            curr = ListNode(values[i])
            prev.next = curr
            prev = curr
        return start
    else:
        return None

