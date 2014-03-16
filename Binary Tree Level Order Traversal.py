#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrder(self, root):
		entire = []
		if root == None:
			return entire
		parent = [root]
		while len(parent) != 0:
			children = []
			listLevel = []
			for x in parent:
				if x == None:
					continue
				listLevel.append(x.val)
				if x.left != None:
					children.append(x.left)
				if x.right != None:
					children.append(x.right)
			parent = children
			entire.append(listLevel)
		return entire

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)

root = None

s = Solution()
print(s.levelOrder(root))