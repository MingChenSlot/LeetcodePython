__author__ = 'mingchen'
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        column = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                column[j] = column[j] + column[j - 1]
        return column[m - 1]

    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        column = [0] * m
        for j in range(0, m):
            if obstacleGrid[j][0] != 1:
                column[j] = 1
            else:
                break

        for i in range(1, n):
            for j in range(0, m):
                if obstacleGrid[j][i] == 1:
                    column[j] = 0
                else:
                    column[j] += (column[j - 1] if j > 0 else 0)
        return column[m - 1]


if __name__ == "__main__":
    s = Solution()
    print s.uniquePaths(1, 1)
    print s.uniquePaths(2, 2)
    print s.uniquePaths(2, 3)
    print "With obstacles"
    a = [
        [0,0,0,0],
        [1,1,0,0],
        [0,0,0,0]
    ]

    b = [[0, 1]]
    print s.uniquePathsWithObstacles(a)
    print s.uniquePathsWithObstacles(b)
