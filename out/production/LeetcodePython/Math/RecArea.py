__author__ = 'mingchen'

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        firstRec = self.computeRec(A, B, C, D)
        seoncdArea = self.computeRec(E, F, G, H)
        l = [A, C, E, G]
        w = [B, D, F, H]
        l.sort()
        w.sort()
        print l, w
        interArea = self.computeRec(l[1], w[1], l[2], w[2])
        return firstRec + seoncdArea - interArea

    def computeRec(self, A, B, C, D):
        return abs(D - B) * abs(C- A)


if __name__ == "__main__":
    s = Solution()
    print s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
