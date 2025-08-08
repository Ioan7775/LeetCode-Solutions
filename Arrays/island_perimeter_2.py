class Solution(object):
    def islandPerimeter(self, grid):
        n,m,per = len(grid),len(grid[0]),0

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    per += 4
                    if i and grid[i - 1][j]:
                        per -= 2
                    if j and grid[i][j - 1]:
                        per -= 2
        return per
        
        

def main():
    sol = Solution()
    grid = [[1,1],[1,1]]
    res = sol.islandPerimeter(grid)
    print(res)

if __name__ == "__main__":
    main()