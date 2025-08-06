class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

        

def main():
    sol = Solution()
    nums = [1,2,3,1]
    res = sol.containsDuplicate(nums)
    print(res)


if __name__ == "__main__":
    main()