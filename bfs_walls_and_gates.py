#leetcode 286. Walls and Gates 
'''
Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''
import collections
#BREATH FIRST SEARCH S
def wallsAndGates(self, rooms: List[List[int]]) -> None:
    if not rooms:
        return []

    #find the 0 and then find the nearest 
    row, col = len(rooms), len(rooms[0])
    q = collections.deque()

    #find all 0 index, and append in a queue to be process 
    for r in range(row):
        for c in range(col):
            if rooms[r][c] == 0:
                q.append((r,c))
    
    # while there is nodes in q to be process, 
    # process each node by taking one step left, right, up and down 
    while q:
        r, c =  q.popleft()
        for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= r+i < row and 0 <= c+j < col and rooms[r][c] < rooms[r+i][c+j]:
                rooms[r+i][c+j] = rooms[r][c] + 1 
                q.append((r+i,c+j))


def wallsAndGates(self, rooms: List[List[int]]) -> None:
    #dfs find and update all linked cells 
    row, col  = len(rooms), len(rooms[0])
    def DFS(rooms, r, c,count):
        for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0<= r+i < len(rooms) and 0<= c+j<len(rooms[0]) and rooms[r][c]<rooms[r+i][c+j]:
                #the above condition will always update the cell to the shoreste path to the door(0)
                rooms[r+i][c+j] = count + 1
                DFS(rooms, r+i, c+j, count+1)
    
    for r in row:
        for c in col:
            if rooms[r][c] == 0:
                DFS(rooms, r, c, 0)


#The only differences between the BFS and DFS is, BFS used a queue to store all the visited cells 

