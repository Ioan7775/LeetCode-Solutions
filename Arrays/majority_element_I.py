class Solution(object):
    def majorityElement(self, nums):
        res,count = 0,0

        for num in nums:
            if count == 0:
                res = num
                count = 1
            elif num == res:
                count += 1
            else:
                count -= 1

        return res

        

def main():
    sol = Solution()
    nums = [2,2,1,1,1,2,2]
    res = sol.majorityElement(nums)
    print(res)


if __name__ == "__main__":
    main()