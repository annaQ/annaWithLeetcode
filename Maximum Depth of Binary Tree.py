# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxDepth(self, root):
		if root == None:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1	

s = Solution()
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(3)
root.left.left.left.right = TreeNode(4)
print(s.maxDepth(root))
