class Solution(object):
    def maxArea(self, height):
        left,right,maxi = 0,len(height) - 1,0

        while left < right:
            latime = right - left
            mini = min(height[left],height[right])

            if latime * mini > maxi:
                maxi = latime * mini
            
            if left < len(height) and right > 0:
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
        
        return maxi


def main():
    sol = Solution()
    height = [1,3,2,5,25,24,5]
    result = sol.maxArea(height)
    print(result)


if __name__ == "__main__":
    main()

#https://onedrive.live.com/view.aspx?resid=CEE996A928F906A4%21s62791f81f9b44841933005e054413688&id=documents&wd=target%28Arrays.one%7CD293D621-B938-5A47-A084-E52EB994EDB7%2F11.%20Container%20with%20most%20water%7C0290F2C1-4D1E-1748-BBAD-5242EE481CAE%2F%29&wdpartid={1C3A3EA0-03CF-0C43-9234-3F183335B1A9}{1}&wdsectionfileid=CEE996A928F906A4!sa2535b6ddf2a43cf8643f191d27eb118
#onenote:https://d.docs.live.net/cee996a928f906a4/Documents/Info/Arrays.one#11.%20Container%20with%20most%20water&section-id={D293D621-B938-5A47-A084-E52EB994EDB7}&page-id={0290F2C1-4D1E-1748-BBAD-5242EE481CAE}&end