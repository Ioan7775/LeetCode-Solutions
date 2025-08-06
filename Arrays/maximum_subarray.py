class Solution(object):
    def maxSubArray(self, nums):
       maxSub = nums[0]
       currSum = 0

       for num in nums:
           if currSum < 0:
               currSum = 0
           currSum += num
           maxSub = max(maxSub,currSum)
           
       return maxSub
           

def main():
    sol = Solution()
    height = [-2,1,-3,4,-1,2,1,-5,4]
    result = sol.maxSubArray(height)
    print(result)


if __name__ == "__main__":
    main()