#Number of Islands 
"""
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
#DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0 
        
        def dfs(grid, r, c):
            row, col = len(grid), len(grid[0])
            if (r<0 or r>=row or c<0 or c>= col or grid[r][c] == '0'):
                return 
            #if the grid cell is 1 and is part of te island, we mark it as visited and change it to 0 
            grid[r][c] = '0'
            #four direction fo move te cell, up, down, left, right 
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)

        island =0 
        rows, cols = len(grid), len(grid[0])

        for r in rows:
            for c in cols:
                if grid[r][c] == '1':
                    island +=1 
                    dfs(grid, r, c)
        
        

