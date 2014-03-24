#Given a string, find longest substring which contains just two unique characters
#what about same length? Give back first one

chars = []
max = ""
first = 0
second = 0

def twoUnique(str):
	if str == None or len(str)<=2:
		return str
	cur = 0
	while cur < len(str):
		if inChar(cur):
			cur = cur + 1
		elif second - first > len(max):
			max = str[first:second]     #replace now
		else:
			first = second
			second = cur
			chars = chars[1:]
			chars.extend(str[second])


def inChar(cur):
	if str[cur] in chars:
		return True
	if len(chars)==0:
		chars.extend(str[cur])
		first = cur
		return True
	if len(chars)==1:
		chars.extend(str[cur])
		second = cur
		return True
	return False


twoUnique("AAAABBCCDDDDDA")
#cur goes through entire string, first denotes the first unique char index, second so. 
#chars contains currently two unique chars, max is the current max substring