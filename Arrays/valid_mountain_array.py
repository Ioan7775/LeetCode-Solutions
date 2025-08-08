class Solution(object):
    def validMountainArray(self, arr):
        length,i = len(arr),1

        if length < 3:
            return False
        
        while i < length and arr[i - 1] < arr[i]:
            i += 1
        if i == 1:
            return False
        
        while i < length and arr[i - 1] > arr[i]:
            i += 1
        if i != length or arr[length - 1] >= arr[length - 2]:
            return False
        
        return True

        

def main():
    sol = Solution()
    arr = [0,1,2,3,4,5,6,7,8,9]
    res = sol.validMountainArray(arr)
    print(res)


if __name__ == "__main__":
    main()