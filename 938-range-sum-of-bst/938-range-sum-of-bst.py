# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # low 찾고, high 찾고 사이 값 더하기
        
#         # 1. 모든 노드 찾고 low, high 사이 더하기 - 비효율적
#         if not root:
#             return 0
        
#         return (root.val if low <= root.val <= high else 0) + \
#                 self.rangeSumBST(root.left, L, R) + \
#                 self.rangeSumBST(root.right, L, R)
        
#         # 2. DFS (재귀)가지치기로 성능향상
        
#         def dfs(node: TreeNode):
#             if not node:
#                 return 0
            
#             if node.val < low:
#                 return dfs(node.right)
#             elif node.val > high:
#                 return dfs(node.left)
#             return node.val + dfs(node.left) + dfs(node.right)
        
#         return dfs(root)
    
#         # 3. DFS 반복구조
        
#         stack, sum = [root], 0
        
#         while stack:
#             node = stack.pop()
#             if node:
#                 if node.val > low:
#                     stack.append(node.left)
#                 if node.val < high:
#                     stack.append(node.right)
#                 if low <= node.val <= high:
#                     sum += node.val
                    
                    
#         return sum


        # 4. BFS 반복구조
        
        stack, sum = collections.deque([root]), 0
        
        while stack:
            node = stack.popleft()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
                    
        return sum
    