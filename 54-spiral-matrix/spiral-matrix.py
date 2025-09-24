class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = -1, len(matrix[0])
        t, b = -1, len(matrix)
        res = []

        x = y = 0
        while x in range(l, r) and y in range(t, b):
            # move right
            while y < r:
                res.append(matrix[x][y])
                y += 1
            y -= 1
            t += 1 # move our top border down one row
            # move down
            x += 1
            while x < b:
                res.append(matrix[x][y])
                x += 1
            x -= 1
            r -= 1 # move our rightside border to the left
            # move left one
            y -= 1
            # if we're all done moving around
            if x <= t or x >= b or y <= l or y >= r: return res
            while y > l:
                res.append(matrix[x][y])
                y -= 1
            y += 1
            b -= 1 # move bottom boundary up one
            # move up one
            x -= 1
            while x > t:
                res.append(matrix[x][y])
                x -= 1
            x += 1
            l += 1 # move left boundary to the right once
            y += 1 # shift to right and start over..
        return res