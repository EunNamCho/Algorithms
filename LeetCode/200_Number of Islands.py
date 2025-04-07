from typing import List

class Solution:
    @classmethod
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        dirs = [(1,0),
                (0,1),
                (-1,0),
                (0,-1)]
        m,n = len(grid), len(grid[0])

        def dfs(answer):
            for start_y, row in enumerate(grid):
                for start_x, _ in enumerate(row):
                    if grid[start_y][start_x]=="1":
                        answer += 1
                        dfs2((start_x, start_y), grid)
            return answer
                        
        def dfs2(start_point, grid):
            start_x, start_y = start_point
            if grid[start_y][start_x]=="1":
                grid[start_y][start_x] = 0
                for dir in dirs:
                    dir_x, dir_y = dir
                    if (0 <= start_y + dir_y < m) and (0 <= start_x + dir_x < n):
                        dfs2((start_x + dir_x, start_y + dir_y), grid)
        
        return dfs(answer)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
print(Solution.numIslands(grid))
