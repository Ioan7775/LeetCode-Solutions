class Solution(object):
    def removeDuplicates(self, nums):
        length,k,i = len(nums),0,0

        while i < length:
            nums[k] = nums[i]
            j = i + 1
            while j < length and nums[i] == nums[j]:
                j += 1
            i,k = j,k + 1
        
        print(nums)
        return k
        

def main():
    sol = Solution()
    nums = [1,1,2]
    result = sol.removeDuplicates(nums)
    print(result)


if __name__ == "__main__":
    main()