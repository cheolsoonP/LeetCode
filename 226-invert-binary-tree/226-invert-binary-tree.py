# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
#         # 1. 파이썬다운 풀이
        
#         if root:
#             root.left, root.right = \
#                 self.invertTree(root.right), self.invertTree(root.left)
#             return root
#         return None
    
    
#         # 2. 반복구조
#         queue = collections.deque([root])
        
#         while queue:
#             node = queue.popleft()
#             # 부모 노드로부터 하향식 스왑
#             if node: 
#                 node.left, node.right = node.right, node.left
                
#                 queue.append(node.left)
#                 queue.append(node.right)
#         return root

        # 3. 반복구조 DFS 후위 순회
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            
            if node:
                stack.append(node.left)
                stack.append(node.right)
                
                node.left, node.right = node.right, node.left
                
        return root
        