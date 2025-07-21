def twoSum(nums, target):
    res = []
    for i in range(len(nums)-1,-1,-1):
        remainder = target - nums[i]
        if remainder in nums:
            idx = nums.index(remainder)
            if i != idx:
                res = [i,idx]

    return res

def main():
    print(twoSum([3,3],6))

if __name__ == '__main__':
    main()