# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param inorder, a list of integers
	# @param postorder, a list of integers
	# @return a tree node
	def buildTree(self, inorder, postorder):
		
		if len(inorder) == 0 or len(postorder) != len(inorder):
			print("None")
			return None

		#postorder's last one is the root
		root = TreeNode(postorder[-1])
		print("root", root.val)
		print("in:",inorder)
		print("post:",postorder)
		if len(inorder) == 1:
			return root
		#seperate the lists	in to two children's
		root_index = inorder.index(postorder[-1]) 
		print("sperate at:", root_index)
		#inorder list is divided by root, first part is for left child
		left_in = inorder[:root_index]
		print("left_in",left_in)
		right_in  = inorder[root_index + 1 :]
		print("right_in",right_in)
		#postorder list should have the first part for left child, as long as the inorder list
		left_post = postorder[:len(left_in)]
		print("left_post",left_post)
		right_post = postorder[len(left_in) : -1]
		print("right_post",right_post)
		root.left = self.buildTree(left_in, left_post)
		root.right = self.buildTree(right_in, right_post)

		return root

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

postorder 	= [4,1,3,10,11,8,2,7]
inorder 	= [4,10,3,1,7,11,8,2]
s = Solution()
root = s.buildTree(inorder, postorder)
print(s.levelOrder(root))
