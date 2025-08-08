class Solution(object):
    def sortArrayByParity(self, nums):
        left,right = 0,len(nums) - 1

        while left < right:
            if nums[left] % 2 == nums[right] % 2:
                if nums[left] % 2 == 0:
                    left += 1
                else:
                    right -= 1
            else:
                if nums[left] % 2 == 1:
                    nums[left],nums[right] = nums[right],nums[left]
                else:
                    left += 1
                    right -= 1
        
        return nums
                    
        

def main():
    sol = Solution()
    nums = [3,1,2,4]
    res = sol.sortArrayByParity(nums)
    print("res = ",res)

if __name__ == "__main__":
    main()