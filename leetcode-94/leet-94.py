# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root1 = [1,None,2,3]
root2 = []
root3 = [1]

print(TreeNode(root1))

# class Solution(object):
#     def inorderTraversal(root1):
#         result = []
#         def inorder(root):
#             if not root:
#                 return
#             inorder(root.left)
#             result.append(root.val)
#             inorder(root.right)
#         inorder(root1)
#         print(result)