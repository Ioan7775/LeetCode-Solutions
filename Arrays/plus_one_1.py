class Solution(object):
    def plusOne(self, digits):
        length = len(digits)
        if digits[length - 1] < 9:
            digits[length - 1] += 1
        else:
            i = length - 1
            while i >= 0 and digits[i] > 8:
                digits[i] = 0
                i -= 1
            if i == -1:
                digits.insert(0,1)
            else:
                digits[i] += 1

        return digits

def main():
    sol = Solution()
    nums = [8,9,9,9]
    result = sol.plusOne(nums)
    print(result)


if __name__ == "__main__":
    main()


#https://onedrive.live.com/view.aspx?resid=CEE996A928F906A4%21s62791f81f9b44841933005e054413688&id=documents&wd=target%28Arrays.one%7CD293D621-B938-5A47-A084-E52EB994EDB7%2F66.Plus%20One%7C8920BB31-7637-8944-B28F-9E0EB2FF291A%2F%29&wdpartid={7658686B-2020-8B44-9D47-3D0594F4884D}{1}&wdsectionfileid=CEE996A928F906A4!sa2535b6ddf2a43cf8643f191d27eb118
#onenote:https://d.docs.live.net/cee996a928f906a4/Documents/Info/Arrays.one#66.Plus%20One&section-id={D293D621-B938-5A47-A084-E52EB994EDB7}&page-id={8920BB31-7637-8944-B28F-9E0EB2FF291A}&end