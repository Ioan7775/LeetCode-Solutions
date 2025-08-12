class Solution(object):
    dir_i = [1,-1,0,0]
    dir_j = [0,0,-1,1]

    def inside(self,a,b):
        return 0 <= a < self.m and 0 <= b < self.n
    
    def fill(self, i, j):
        stack = [(i, j)]

        while stack:
            x, y = stack.pop()
            self.area += 1

            for ind in range(4):
                new_x = x + self.dir_i[ind]
                new_y = y + self.dir_j[ind]
                if self.inside(new_x,new_y) and self.grid[new_x][new_y] == 1:
                    stack.append((new_x, new_y))
                    self.grid[new_x][new_y] = -1

    def maxAreaOfIsland(self, grid):
        self.grid,self.area,maxArea = grid,0,0
        self.m,self.n = len(grid),len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if(grid[i][j] == 1):
                    grid[i][j] = -1
                    self.area = 0
                    self.fill(i,j)
                    maxArea = max(maxArea,self.area)

        return maxArea
        

def main():
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    res = sol.maxAreaOfIsland(grid)
    print(res)

if __name__ == "__main__":
    main()