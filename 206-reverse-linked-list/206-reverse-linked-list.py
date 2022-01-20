# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         # 1. 재귀
#         def reverse(node: ListNode, prev: ListNode = None):
#             if not node:
#                 return prev
#             next, node.next = node.next, prev
#             return reverse(next, node)
        
#         return reverse(head)
    
        
        # 2. 반복
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev
    