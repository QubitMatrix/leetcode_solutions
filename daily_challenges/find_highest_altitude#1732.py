class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxval=0
        altitude=0
        for x in gain:
            altitude+=x
            maxval=max(maxval,altitude)
        return maxval
