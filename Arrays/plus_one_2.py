class Solution(object):
    def plusOne(self, digits):
        length = len(digits)
        for i in range(length-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0,1)
        return digits
        

def main():
    sol = Solution()
    nums = [8,9,9,9]
    result = sol.plusOne(nums)
    print(result)


if __name__ == "__main__":
    main()