# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def inorderTraversal(self, root):
		if root == None:
			return []
		stack = []
		list = []
		if root == None:
			return None
		while True:
			while root.left != None:
				stack.append(root)
				root = root.left
			list.append(root.val)
			while len(stack) > 0 and root.right == None:
				root = stack[-1]
				stack = stack[:-1]
				list.append(root.val)
			if root.right != None:
				root = root.right
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
q.left.left.left.left = TreeNode(4)
q.left.left.left.right = TreeNode(4)
q.left.left.left.right.right = TreeNode(5.5)
q.left.left.left.right.left = TreeNode(5)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.inorderTraversal(None))


#while root.LC exist, push, root = root.left
#now LC not, so print root
#if right child exist, root = right, go back from beginning
#else, root is a leafm root = stack.pop, print root, 
#while root just have no right child, pop-print all the way back until stack empty
#root = root.right,go back from beginning

