# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def preorderTraversal(self, root):
		stack = []
		list = []
		if root == None:
			return None
		while True:
			list.append(root.val)
			if root.left != None and root.right != None:
				stack.append(root)
			if root.left != None:
				root = root.left
			elif root.right != None:
				root = root.right
			elif len(stack) > 0:
				root = stack[-1].right
				stack = stack[:-1]
			else:
				break
		return list
			

s = Solution()
q = TreeNode(0)
q.left = TreeNode(1)
q.right = TreeNode(1)
q.right.left = TreeNode(2)
q.right.right = TreeNode(2)
q.left.left = TreeNode(2)
q.left.left.left = TreeNode(3)
q.left.left.left.right = TreeNode(4)
q.left.left.left.right.right = TreeNode(5)
q.left.left.left.right.left = TreeNode(5)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.preorderTraversal(root))


