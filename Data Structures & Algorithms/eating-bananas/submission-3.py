import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        temp_k = 1
        while(min_k <= max_k):
            mid_k = (min_k+max_k)//2
            total_hours = 0
            print(f"min_k: {min_k}")
            print(f"max_k: {max_k}")
            print(f"mid_k: {mid_k}")
            for p in piles:
                hours = math.ceil(p/mid_k)
                total_hours+=hours
            print(f"total hours: {total_hours}")
            if (total_hours <= h):
                print(f"HIGH")
                max_k=mid_k-1
                temp_k = mid_k
            elif (total_hours > h):
                print(f"LOW")
                min_k=mid_k+1
        return temp_k

    """
    piles=[1,1,1,6,6,6], h=9
    min_k=1
    max_k=6

    mid_k=3

    total_hours=9
    k=3
    """