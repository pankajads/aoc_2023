import sys
import re
from collections import defaultdict

def solution2(nums):
    result = 0
    for k,v in nums.items():
        if len(v)==2:
            result += v[0]*v[1]
    
    return result

def solution1(G,R,C):
    result = 0
    nums = defaultdict(list)
    for r in range(len(G)):
      gears = set() # positions of '*' characters next to the current number
      n = 0
      has_part = False
      print(len(G[r]))
      for c in range(len(G[r])+1):
        if c<C and G[r][c].isdigit():
          n = n*10+int(G[r][c])
          for rr in [-1,0,1]:
            for cc in [-1,0,1]:
              if 0<=r+rr<R and 0<=c+cc<C:
                ch = G[r+rr][c+cc]
                if not ch.isdigit() and ch != '.':
                  has_part = True
                if ch=='*':
                  gears.add((r+rr, c+cc))
        elif n>0:
          for gear in gears:
            nums[gear].append(n)
          if has_part:
            result += n
          n = 0
          has_part = False
          gears = set()

    return result, nums

file1="sample.txt" #puzzle 1
#main function
if __name__ == "__main__":
    solution_1 = 0
    solution_2 = 0
    #Reading Input file and parse it line by line
    filehandler = open(file1).read().strip()
    lines = filehandler.split('\n')
    grid = [[c for c in line] for line in lines]
    #print(grid)
    row_count = len(grid)
    #print(row_count)
    col_count = len(grid[0])
    #print(col_count)
    
    results = solution1(grid,row_count,col_count)
    print(results[0])
    print(solution2(results[1]))

 
