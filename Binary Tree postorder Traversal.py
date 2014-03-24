# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
	def postorderTraversal(self, root):
		if root == None:
			return []
		stack_root = []
		stack_dir = []
		list = []
		while True:
			while root.left != None or root.right != None:
				stack_root.append(root)
				#have both children, so need to visit RC next time
				stack_dir.append(root.left != None and root.right != None)
				root = root.left if root.left != None else root.right
			#root is a leaf now
			list.append(root.val)
			while len(stack_dir) > 0:
				dir = stack_dir[-1]
				stack_dir = stack_dir[:-1]
				root = stack_root[-1]
				#if false, we dont need to deal with RC anymore
				if not dir:
					stack_root = stack_root[:-1]
					list.append(root.val)
					# go on popping up
				else:
					root = root.right
					stack_dir.append(False)
					break # go down again
			if len(stack_dir) == 0:
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
q.left.left.left.right.right = TreeNode(6)
q.left.left.left.right.left = TreeNode(5)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.postorderTraversal(q))



#<while> root != leaf, push 2 stacks, root = root.left> right, F is go left, T if go right </while>
#now root is a leaf, print root.val
#root = stack.pop, the other stack pop the direction, if F, then it has only tried the LC, try RC
#else it has tried both, so go up


