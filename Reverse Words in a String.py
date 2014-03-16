# Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        list = s.split(" ")
        list.reverse()
        newStr = ""
        for str in list:
	        if(str):
		        newStr = newStr + str + " "
        return newStr.strip()

s = " the sky  is blue the sky  is blue"
sl = Solution()
print(sl.reverseWords(s))