class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        length,closest,res = len(nums),1e9,0

        for i in range(length - 1):
            j,k = i+1,length - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum - target) < closest:
                    closest = abs(sum - target)
                    res = sum
                else:
                    if sum < target:
                        j += 1
                    else:
                        k -= 1
        return res

            

def main():
    sol = Solution()
    nums = [4,0,5,-5,3,3,0,-4,-5]
    res = sol.threeSumClosest(nums,-2)
    print(res)


if __name__ == "__main__":
    main()