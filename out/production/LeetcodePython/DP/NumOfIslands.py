__author__ = 'mingchen'

# @param grid, a list of list of characters
# @return an integer
def numIslands(grid):
    num_islands = 0

    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value is "1":
                if j > 0 and row[j - 1] == "1":
                    if i > 0 and grid[i-1][j] is not "0" and grid[i-1][j - 1] is "0":
                        num_islands -= 1
                else:
                    if i == 0 or grid[i-1][j] is "0":
                        num_islands += 1
    return num_islands

if __name__ == "__main__":
    a = ["1", "0", "1"]
    b = ["0", "0", "0"]
    c = ["1", "1", "1"]
    x = []
    x.append(a)
    x.append(c)
    x.append(b)
    x = [["1"], ["1"]]
    print numIslands(x)









