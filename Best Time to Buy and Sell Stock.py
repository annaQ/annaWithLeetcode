# Best Time to Buy and Sell Stock II
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
#(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time 
#(ie, you must sell the stock before you buy again).

class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit1(self, prices):
		#whether I have bought or not
		hold = False
		profit = 0
		for i in range(0,len(prices) - 1):
			#if next day it goes up, we want to have it today
			if not hold and (prices[i + 1] > prices[i]):
				hold = True
				print("Buy at day " , i)
				inPrice = prices[i]
			if hold and (prices[i + 1] <= prices[i]):
				hold = False
				profit = profit + prices[i] - inPrice
		return profit
	def maxProfit(self, prices):
		#whether I have bought or not
		hold = False
		profit = 0
		for i in range(0,len(prices) - 1):
			profit = profit + max(0,prices[i+1] - prices[i])
		return profit

s = Solution()
print(s.maxProfit([1,2,3,2,1,2,5]))