class Solution(object):
    def moveZeroes(self, nums):
        k,length = 0,len(nums)

        for num in nums:
            if num:
                nums[k] = num
                k += 1
        nums[k:length] = [0] * (length - k)
        
           


def main():
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    print(nums)


if __name__ == "__main__":
    main()