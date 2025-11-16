class Solution:
    def reverse(self, x: int) -> int:
        out_bounds_low, out_bounds_high = -2 ** 31, 2 ** 31 - 1
        if x <= out_bounds_low or x >= out_bounds_high: return 0
        s_x = str(x)
        neg = False
        if s_x[0] == '-':
            s_x = s_x[1:]
            neg=True
        if neg: new_int =  -1 * int(s_x[::-1])
        else: new_int = int(s_x[::-1])
        if new_int <= out_bounds_low or new_int >= out_bounds_high: return 0
        return new_int
