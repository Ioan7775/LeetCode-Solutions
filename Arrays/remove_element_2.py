class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

def main():
    sol = Solution()
    nums = [0,1,2,2,3,0,4,2]
    res = sol.removeElement(nums,2)
    print("res = ",res)
    print("nums = ",nums)


if __name__ == "__main__":
    main()