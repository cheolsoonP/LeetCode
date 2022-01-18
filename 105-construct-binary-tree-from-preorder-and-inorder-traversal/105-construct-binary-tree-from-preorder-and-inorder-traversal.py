# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder - 전위 순회
        # inorder - 중위 순회
        
        if inorder:
            # 전위 - 0번째 값 = root, 중위에서 찾으면 왼쪽과 오른쪽으로 나눔
            
            index = inorder.index(preorder.pop(0))

            # 
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])

            return node