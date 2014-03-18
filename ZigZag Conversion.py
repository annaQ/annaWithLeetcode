# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
	# @return a string
	def convert(self, s, nRows):
		if s == None or nRows == 0:
			return None
		if nRows == 1 or nRows >= len(s):
			return s
		convertedStr = ""
		unitLen = 2 * nRows - 2
		unit = len(s)/unitLen
		#print each row in outer loop
		for row in xrange(0,nRows):
			for i in xrange(0,unit+1):
				if row == 0 or row == nRows - 1:
					if i * unitLen + row < len(s):
						convertedStr = convertedStr+s[i * unitLen + row]
				else:
					if (i * unitLen + row) < len(s):
						convertedStr = convertedStr+s[i * unitLen + row]
					if ((i + 1) * unitLen - row) < len(s):
						convertedStr = convertedStr+s[(i + 1) * unitLen - row]
				if len(convertedStr) == len(s):
					return convertedStr



s = Solution()
str = "PAYPALISHIRING"
str = "AC"
print(s.convert(str,3))
 
#PAHN APLSIIG YIR
#PAHN APLSIIG YIR

