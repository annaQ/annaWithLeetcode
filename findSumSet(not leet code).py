#The goal here is to find all the sets of integers which sum up to a given number
#for example: 2 = 1+1; 3 = 1 + 1 + 1 = 1 + 2; 4= 1 + 1 + 1 + 1 = 2 + 1 + 1 = 3 + 1 = 2 + 2
def findSumSets(n):
	#for number n, there could be the very basic n-size set, sum up of n 1s, to two-element sets
	#They will be all different from each other while none empty
	basic = []
	for x in xrange(0,n):
		basic.append(1)
	sets = [basic]  #now it is a list of list
 	for x in xrange(2,n):
		sets.append(findSizeNSets(n,x))
	print(sets)

def findSizeNSets(sum, size):
	if size == 2:
		set = []
		for a in xrange(1,1 + sum/2):
			set.append([a,sum-a])
		return set
	else:
		sets = []
		for a in xrange(1,sum/2):
			set = findSizeNSets(sum - a,size - 1)
			set.append(a)
			sets.extend(set)
		return sets


findSumSets(5)