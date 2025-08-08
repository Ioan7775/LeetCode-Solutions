class Solution(object):
    def majorityElement(self, nums):
        res1,count1,res,length = 0,0,[],len(nums)
        res2,count2 = 0,0

        for num in nums:
            if num == res1:
                count1 += 1
            elif num == res2:
                count2 += 1
            elif count1 == 0:
                res1 = num
                count1 = 1         
            elif count2 == 0 and num != res1:
                res2 = num
                count2 = 1
            
            if num != res1 and num != res2:
                count1 -= 1
                count2 -= 1
        
        count1,count2 = 0,0

        for num in nums:
            if num == res1:
                count1 += 1
            if num == res2:
                count2 += 1
        
        if count1 > length // 3:
            res.append(res1)
        if res1 != res2 and count2 > length // 3:
            res.append(res2)
        
        return res
        



def main():
    sol = Solution()
    nums = [2,9,1,9,4,3,8,9]
    res = sol.majorityElement(nums)
    print(res)


if __name__ == "__main__":
    main()