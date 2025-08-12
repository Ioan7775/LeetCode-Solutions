class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        length,res = len(nums),[]

        for i in range(length - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j,k = i+1,length - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return res

            



def main():
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    res = sol.threeSum(nums)
    print(res)


if __name__ == "__main__":
    main()