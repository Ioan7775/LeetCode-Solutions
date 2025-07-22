class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res


def main():
    sol = Solution()
    nums = [1,1,2]
    result = sol.singleNumber(nums)
    print(result)


if __name__ == "__main__":
    main()


#https://onedrive.live.com/view.aspx?resid=CEE996A928F906A4%21s62791f81f9b44841933005e054413688&id=documents&wd=target%28Arrays.one%7CD293D621-B938-5A47-A084-E52EB994EDB7%2F136.%20Single%20number%7C2DE7EDC7-8114-7749-8803-9F5F881287B2%2F%29&wdpartid={E292F46D-2B33-3C49-BC68-13706D47372A}{1}&wdsectionfileid=CEE996A928F906A4!sa2535b6ddf2a43cf8643f191d27eb118
#onenote:https://d.docs.live.net/cee996a928f906a4/Documents/Info/Arrays.one#136.%20Single%20number&section-id={D293D621-B938-5A47-A084-E52EB994EDB7}&page-id={2DE7EDC7-8114-7749-8803-9F5F881287B2}&end