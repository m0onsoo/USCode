##포인터 2개로 양쪽 끝에서 출발하여 더 작은 값을 가진 쪽의 포인터를 안쪽으로 이동하는게 main idea
# 왜 작은쪽을 이동하냐? -> 가로폭은 무조건 줄어드므로 넓이를 늘리려면 세로 높이가 커져야 한다, 세로 높이는 min 값으로 정해지므로 작은 쪽 포인터를 움직이지 않으면 세로 높이는 절대 커질 수 없음

###Leet Code Style
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_area=0

        while l<r:
            width = r-l
            h = min(heights[l],heights[r])
            area = width*h
            max_area = max(area, max_area)
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1
        
        return max_area
    
###Korean Coding Test Style
heights = list(map(int, input().split()))
l=0
r=len(heights)-1
max_area=0

while l<r:
    width=r-l
    h=min(heights[l], heights[r])
    area=width*h
    max_area=max(area,max_area)
    if heights[l]<heights[r]:
        l=l+1
    else:
        r=r-1

print(max_area)
                 