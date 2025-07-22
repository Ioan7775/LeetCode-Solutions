class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
        

def main():
    sol = Solution()
    nums = [1,1,2]
    result = sol.removeDuplicates(nums)
    print(result)


if __name__ == "__main__":
    main()