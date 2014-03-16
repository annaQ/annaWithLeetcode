# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution:
	def __init__(self):
		self.cache = {1:1, 2:2}
	# @param n, an integer
	# @return an integer
	def climbStairs(self, n):
		if(n not in self.cache):
			self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
		return self.cache[n]
s=Solution()
print(s.climbStairs(100))




