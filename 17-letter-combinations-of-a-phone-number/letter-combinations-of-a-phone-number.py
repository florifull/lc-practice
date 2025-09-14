class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits: return []
        res = []
        def dfs(i, localArr):
            if i >= len(digits):
                res.append(''.join(localArr[:]))
                return
            chars = digitToChar[digits[i]]
            for j in range(len(chars)):
                localArr.append(chars[j])
                dfs(i+1, localArr)
                localArr.pop()
        dfs(0, [])
        return res