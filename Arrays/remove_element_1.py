class Solution(object):
    def removeElement(self, nums, val):
        count,length = 0,len(nums)
        while val in nums:
            nums.remove(val)
            count += 1
        nums += [0] * count
        return length - count

def main():
    sol = Solution()
    nums = [0,1,2,2,3,0,4,2]
    res = sol.removeElement(nums,2)
    print("res = ",res)
    print("nums = ",nums)


if __name__ == "__main__":
    main()