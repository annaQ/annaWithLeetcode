class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
		if(num == None or len(num) <= 1):
			return num
		if(len(num) == 2):
			return [[num[0],num[1]],[num[1],num[0]]]
		list = self.permute(num[1:])
		return_list = []
		for sub_list in list:
			for x in xrange(0,len(sub_list)+1):
				sub_list = sub_list[:x].append(num[1:]).append(sub_list[x:])
				return_list.append(sub_list)
		return return_list

s = Solution()
print(s.permute([1,2,2,3]))
