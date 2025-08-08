class Solution(object):
    def searchInsert(self, nums, target):
        left,right = 0,len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return left

def main():
    sol = Solution()
    nums = [1,3,5,6]
    res = sol.searchInsert(nums,2)
    print("res = ",res)

if __name__ == "__main__":
    main()