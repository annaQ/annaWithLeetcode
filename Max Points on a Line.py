import math
#Max Points on a Line 
#Given n points on a 2D plane, find the maximum number of points 
#that lie on the same straight line.

# Definition for a point
class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.x == other.x and self.y == other.y 
		else:
			return False
class vec:
	def __init__(self, fst, snd):
		self.start = fst
		self.vec = Point(snd.x - fst.x,snd.y - fst.y)
		self.stack = [fst,snd]

class Solution:
	# @param points, a list of Points
	# @return an integer
	def maxPoints(self, points):
		#Sorted only with x coord is enough
		points.sort(key = lambda tup: tup[0])
		for i in range(0,len(points)):
			p0 = points[i]
			for j in range(i + 1 , len(points)):
				p1 = points[j]
				if p0 == p1:
					print p0,p1
					max = max + 1
					continue
				else:
					vector = Point(p0.x - p1.x, p0.y - p1.y)

	def same(self,p1, p2):
		return p1[0] == p2[0] and p1[1] == p2[1]



s = Solution()
ps1 = [(3,10),(0,2),(0,2),(3,10)]
s.maxPoints(ps1)
print(ps1)
#expected :4
ps2 = [(0,9),(138,429),(115,359),(115,359),(-30,-102),(230,709),(-150,-686),(-135,-613),(-60,-248),(-161,-481),(207,639),(23,79),(-230,-691),(-115,-341),(92,289),(60,336),(-105,-467),(135,701),(-90,-394),(-184,-551),(150,774)]
#Expected: 12
s.maxPoints(ps2)
