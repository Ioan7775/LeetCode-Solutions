class Solution(object):
    def maxProfit(self, prices):
        l,r,length,maxP = 0,1,len(prices),0

        while r < length:
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxP = max(diff,maxP)
            else:
                l = r
            r += 1
        return maxP

            



def main():
    sol = Solution()
    prices = [7,1,5,3,6,4]
    result = sol.maxProfit(prices)
    print(result)


if __name__ == "__main__":
    main()