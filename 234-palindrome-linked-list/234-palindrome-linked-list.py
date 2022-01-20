# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
#         q = []
        
#         node = head
        
#         while node is not None:
#             q.append(head.val)
#             node = node.next
        
#         for i in q:
#             if q[i] != q.pop():
#                 return False
        
#         return True

        q = collections.deque()
        
        node = head
        
        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True