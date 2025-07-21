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




#https://onedrive.live.com/edit.aspx?resid=CEE996A928F906A4!s62791f81f9b44841933005e054413688&migratedtospo=true&wd=target%28Arrays.one%7Cd293d621-b938-5a47-a084-e52eb994edb7%2FTwoSum%7C9584416d-7be7-f844-affc-5287f4658ecf%2F%29&wdorigin=NavigationUrl
