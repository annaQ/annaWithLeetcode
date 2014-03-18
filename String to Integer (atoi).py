import re
# Implement atoi to convert a string to an integer.

# Hint: Carefully consider all possible input cases. 
# If you want a challenge, please do not see below and ask yourself what are the possible input cases.
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). 
# The string can contain additional characters after those that form the integral number, 
# which are ignored and have no effect on the behavior of this function.

class Solution:
	# @return an integer
	def atoi(self, str):
		if str == None or str.strip() == "":
			return 0
		match = re.search('^[+-]?\d+\D?',str.strip())
		if match:
			extra = match.group()
			if re.search('\D$',extra):
				val = float(extra[:-1])
			else:
				val = float(extra)
			val = min(2147483647, val)
			val = max(-2147483648,val)
		else:
 			val = 0				
		return int(val)

s = Solution()
print(s.atoi("-1222"))