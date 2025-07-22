class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                
        return prefix
        

def main():
    sol = Solution()
    words = ["flower","flow","flight"]
    result = sol.longestCommonPrefix(words)
    print(result)


if __name__ == "__main__":
    main()

# https://onedrive.live.com/view.aspx?resid=CEE996A928F906A4%21s62791f81f9b44841933005e054413688&id=documents&wd=target%28Arrays.one%7CD293D621-B938-5A47-A084-E52EB994EDB7%2F14.Longest%20Common%20Prefix%7CEF9E4754-A301-6042-AFCB-49C144CBE9DE%2F%29&wdpartid={51C9AE55-6A58-E44A-97FF-A8A79E43BE04}{1}&wdsectionfileid=CEE996A928F906A4!sa2535b6ddf2a43cf8643f191d27eb118
# onenote:https://d.docs.live.net/cee996a928f906a4/Documents/Info/Arrays.one#14.Longest%20Common%20Prefix&section-id={D293D621-B938-5A47-A084-E52EB994EDB7}&page-id={EF9E4754-A301-6042-AFCB-49C144CBE9DE}&end