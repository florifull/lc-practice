class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack = [d, e, e] "edbbcccbdaa", k = 3 ... len(stack) >= k-1
        stack = [s[0]]
        for i in range(1, len(s)):
            # possibility of duplicate removal instance..
            if len(stack) >= k-1:
                window = stack[-1 * (k-1):]
                duplicate = True
                for w in window:
                    if w != s[i]:
                        stack.append(s[i])
                        duplicate = False
                        break
                if not duplicate: continue
                # found that we do have duplicates up to k-1 in window
                j = 0
                while j < k-1:
                    stack.pop()
                    j += 1
                continue
            stack.append(s[i])
        return ''.join(stack)
                
            