class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if(prices[i]-minp>profit):
                profit=prices[i]-minp
            if(prices[i]<minp):
                minp=prices[i]

        return profit