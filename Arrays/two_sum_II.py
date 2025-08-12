class Solution(object):
    def twoSum(self, numbers, target):
        l,r,res = 0,len(numbers) - 1,[]

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                res = [l+1,r+1]
                break
            elif sum < target:
                l += 1
            else:
                r -= 1
        return res



def main():
    sol = Solution()
    numbers = [2,7,11,15]
    res = sol.twoSum(numbers,9)
    print(res)


if __name__ == "__main__":
    main()