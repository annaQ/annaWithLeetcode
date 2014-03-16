# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
		if len(inorder) == 0 or len(postorder) != len(inorder):
			return None
		#postorder's last one is the root
		root = TreeNode(postorder[-1])
		if len(inorder) == 1:
			return root
		#seperate the lists	in to two children's
		root_index = inorder.index(postorder[-1]) 
		#inorder list is divided by root, first part is for left child
		left_in = inorder[:root_index]
		right_in  = inorder[root_index + 1 :]
		#postorder list should have the first part for left child, as long as the inorder list
		left_post = postorder[:len(left_in)]
		right_post = postorder[len(left_in) : -1]
		root.left = self.buildTree(left_in, left_post)
		root.right = self.buildTree(right_in, right_post)
		return root       