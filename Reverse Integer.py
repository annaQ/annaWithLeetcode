# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

# How to deal with the possible overflow?(although no test case on that)

class Solution:
	# @return an integer
	def reverse(self, x):
		if x == 0 or x == None:
			return x
		new = 0
		tmp = abs(x)
		dir = tmp / x
		while tmp>0:
			digit = tmp % 10
			new = digit + new * 10
			tmp = tmp / 10
		return(new * dir)

s = Solution()
print(s.reverse(-1234))