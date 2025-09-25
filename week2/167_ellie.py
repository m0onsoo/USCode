## 이것 또한 투포인터가 메인 idea
# 포인터는 양 끝 쪽에서 시작하고 
# 포인터가 가리키는 값의 합이 target보다 작을시에 왼쪽에 있는 포인터가 안쪽으로 이동,
# target보다 클 경우 오른쪽에 있는 포인터가 안쪽으로 이동!

# 처음에 제대로 확인 못한 부분
# 1. 1-indexed array라는 부분
# -> return할 때 +1씩 해줘야함
# 2. -1000<= numbers[i] <=1000 이라 음수도 가능하다는 점

###Leet Code Style
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while l<r:
            s=numbers[l]+numbers[r]
            if s>target:
                r-=1
            elif s<target:
                l+=1
            else:
                return [l+1,r+1]