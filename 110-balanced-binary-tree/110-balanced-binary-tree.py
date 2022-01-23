# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # 차이값 상태값 계산
        
        def check(node):
            
            # 맨 마지막 노드일 경우 0 리턴
            if not node:
                return 0
            
            
            left = check(node.left)
            right = check(node.right)
            
            # 왼쪽과 오른쪽의 차이가 1보다 크면 false
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            
            return max(left, right) + 1
        
        return check(root) != -1
    