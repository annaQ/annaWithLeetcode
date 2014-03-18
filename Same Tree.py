# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param p, a tree node
	# @param q, a tree node
	# @return a boolean
	def isSameTree(self, p, q):
		if p == None and q == None:
			return True
		if p == None or q == None or p.val != q.val:
			return False
		return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

s = Solution()
q = TreeNode(0)
q.left = TreeNode(1)
q.right = TreeNode(1)
q.left.left = TreeNode(2)
q.left.left.left = TreeNode(3)
q.left.left.left.right = TreeNode(4)
p = TreeNode(0)
p.left = TreeNode(1)
p.right = TreeNode(1)
p.left.left = TreeNode(2)
p.left.left.left = TreeNode(3)
# p.left.left.left.right = TreeNode(4)
print(s.isSameTree(p,q))
