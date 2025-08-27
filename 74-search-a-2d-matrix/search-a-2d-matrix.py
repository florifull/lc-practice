class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l < r:
            m = (l + r) // 2
            leftM, rightM = matrix[m][0], matrix[m][-1]
            if target < leftM: r = m - 1
            elif target > rightM: l = m + 1
            else:
                # found an array with correct target range (first & last element)
                l = r = m
    # found a target array
        targetArray = matrix[l]
        l, r = 0, len(targetArray) - 1
        while l <= r:
            m = (l + r) // 2
            if targetArray[m] < target: l = m + 1
            elif targetArray[m] > target: r = m - 1
            else:
                return True
        return False
