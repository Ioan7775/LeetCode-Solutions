class Solution(object):
    def isMonotonic(self, nums):
        increasing,decreasing = True,True
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            if nums[i] < nums[i - 1]:
                increasing = False

        return increasing or decreasing
           


def main():
    sol = Solution()
    nums = [1,3,2]
    res = sol.isMonotonic(nums)
    print(res)


if __name__ == "__main__":
    main()