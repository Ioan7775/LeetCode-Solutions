class Solution(object):
    def maxProfit(self, prices):
        length,mini,maxP = len(prices),1e9,0

        for i in range(length):
            mini = min(mini,prices[i])
            diff = prices[i] - mini
            maxP = max(diff,maxP)

        return maxP

            



def main():
    sol = Solution()
    prices = [7,1,5,3,6,4]
    result = sol.maxProfit(prices)
    print(result)


if __name__ == "__main__":
    main()