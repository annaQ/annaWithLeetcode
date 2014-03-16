# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
	def isdigit(self,str):
		try:
			float(str)
			return True
		except ValueError:
			return False
	# @param tokens, a list of string
	# @return an integer
	def evalRPN(self, tokens):
		stack = []
		for str in tokens:
			print(stack)
			print(str)
			if self.isdigit(str):
				stack.append(str)
			else:
				if len(stack) < 2:
					raise Exception()
				else:
					x = (int)(stack[-1])
					y = (int)(stack[-2])
					stack = stack[:-2]
					if str == "+":
						z = x + y
					elif str == "-":
						z = y - x
					elif str == "*":
						z = y * x						
					else:
						z = y * 1.0 / x
					stack.append(z)
		return (int)(stack[0])

s = Solution()
list1 = ["2", "1", "+", "3", "*"]
list2 = ["-4", "13", "5", "/", "+"]
list3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#print(s.evalRPN(list1))
#print(s.evalRPN(list2))
print(6 / -132)
print(s.evalRPN(list3))  # supposed to be 22