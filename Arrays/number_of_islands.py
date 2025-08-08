class Solution(object):
    dir_i = [1,-1,0,0]
    dir_j = [0,0,-1,1]

    def inside(self,a,b):
        return 0 <= a < self.m and 0 <= b < self.n
    
    def fill(self, i, j):
        grid = self.grid
        m, n = self.m, self.n
        dir_i, dir_j = self.dir_i, self.dir_j

        stack = [(i, j)]
        grid[i][j] = "0"

        while stack:
            x, y = stack.pop()
            for ind in range(4):
                new_x = x + dir_i[ind]
                new_y = y + dir_j[ind]
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == "1":
                    grid[new_x][new_y] = "0"
                    stack.append((new_x, new_y))

    def numIslands(self, grid):
        self.grid = grid
        self.m,self.n,count = len(grid),len(grid[0]),0

        for i in range(self.m):
            for j in range(self.n):
                if(grid[i][j] == "1"):
                    self.fill(i,j)
                    count += 1
        return count

def main():
    sol = Solution()
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    res = sol.numIslands(grid)
    print(res)


if __name__ == "__main__":
    main()