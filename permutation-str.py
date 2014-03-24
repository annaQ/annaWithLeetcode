def permutation(str):
	if(str == None or len(str) <= 1):
		return str
	list = permutation(str[:-1])
	largerStr = []
	for miniStr in list:
		for x in xrange(0,len(miniStr)+1):
			if x < len(miniStr) and miniStr[x] == str[-1]:
				continue   #no duplicate
			largerStr.append(miniStr[:x]+str[-1]+miniStr[x:])
	return largerStr

print(permutation("122"))
print(permutation(""))
print(permutation(None))
print(permutation("ILU"))