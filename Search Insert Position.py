# Given a sorted array and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
class Solution:
	# @param A, a list of integers
	# @param target, an integer to be inserted
	# @return integer
	def searchInsert(self, A, target):
		if len(A) == 0:
			return 0
		lb = 0
		ub = len(A) - 1
		while lb <= ub:
			mid = lb + (ub - lb) / 2
			if A[mid] == target:
				return mid
			elif A[mid] > target:
				ub = mid - 1
			else:
				lb = mid + 1
		return ub + 1

s = Solution()
A = [1]
print(s.searchInsert(A,0))