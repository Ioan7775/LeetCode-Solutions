class Solution(object):
    def generate(self, numRows):
        nums,count = [[1],[1,1]],1

        if numRows == 1:
           return [[1]]
        if numRows == 2:
           return nums
       
        while count < numRows:
            temp = [1]
            for i in range(1,count + 1):
               sum = nums[count][i - 1] + nums[count][i]
               temp.append(sum)

            temp.append(1)
            count += 1
            nums.append(temp)

        return nums
           


def main():
    sol = Solution()
    res = sol.generate(5)
    print(res)


if __name__ == "__main__":
    main()