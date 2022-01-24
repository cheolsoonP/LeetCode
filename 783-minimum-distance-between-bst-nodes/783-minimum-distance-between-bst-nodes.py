# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # # 재귀, 중위 순회
    prev = -sys.maxsize
    result = sys.maxsize
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # 왼쪽부터 방문하는 중위순회
        # 1. 왼쪽
        if root.left:
            self.minDiffInBST(root.left)
            
        # 2. 자신
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        
        # 3. 오른쪽
        if root.right:
            self.minDiffInBST(root.right)
        
        
        return self.result
    

#         # 2. 반복, 중위 순회
#         prev = -sys.maxsize
#         result = sys.maxsize
        
#         stack = []
#         node = root
        
#         while stack or node:
#             while node:
#                 stack.append(node)
#                 node = node.left
            
#             node = stack.pop()
            
#             result = min(result, node.val - prev)
#             prev = node.val
            
#             node = node.right
            
#         return result