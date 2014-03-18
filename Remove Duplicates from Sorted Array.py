class Solution:
	# @param a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		if len(A) == 0:
			return 0
		walker = 0
		runner = walker + 1
		while(runner < len(A)):
			if (A[walker] == A[runner]):
				runner = runner + 1  
			else:
				A[walker + 1] = A[runner]
				walker = walker + 1	   
		return walker + 1


s = Solution()
A = [1,2,2,2,2,2,3]
print(s.removeDuplicates(A))