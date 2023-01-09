class Solution:
    def reverseBits(self, n: int) -> int:
        s=str(bin(n))[2:]
        bin_rev="".join(reversed(s))+"0"*(32-len(s))
        return int(bin_rev,2)
