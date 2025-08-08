class Solution(object):
    dir_i = [1,-1,0,0]
    dir_j = [0,0,-1,1]

    def inside(self,a,b):
        return 0 <= a < self.m and 0 <= b < self.n
    
    def perim(self,i,j):
        for poz in [0,self.m - 1]:
            if poz == i:
                self.perimeter += 1
        for poz in [0,self.n - 1]:
            if poz == j:
                self.perimeter += 1

        for ind in range(4):
            new_i = i + self.dir_i[ind]
            new_j = j + self.dir_j[ind]

            if self.inside(new_i,new_j) and self.grid[new_i][new_j] == 0:
                self.perimeter += 1

    def fill(self, i, j):
        stack = [(i, j)]

        while stack:
            x, y = stack.pop()
            self.perim(x,y)

            for ind in range(4):
                new_x = x + self.dir_i[ind]
                new_y = y + self.dir_j[ind]
                if self.inside(new_x,new_y) and self.grid[new_x][new_y] == 1:
                    stack.append((new_x, new_y))
                    self.grid[new_x][new_y] = -1

    def islandPerimeter(self, grid):
        self.grid,self.perimeter = grid,0
        self.m,self.n,count = len(grid),len(grid[0]),0

        for i in range(self.m):
            for j in range(self.n):
                if(grid[i][j] == 1):
                    grid[i][j] = -1
                    self.fill(i,j)
                    break
        return self.perimeter
        
        

def main():
    sol = Solution()
    grid = [[1,1],[1,1]]
    res = sol.islandPerimeter(grid)
    print(res)

if __name__ == "__main__":
    main()