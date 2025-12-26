from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                if num < 0:
                    # 음수일 경우 2의 보수로 변환. 이렇게 할 경우 32bit 양수의 최대값을 넘어서 기존 리스트에 있던 양수값과 겹치지 않음
                    num = num & (2**32-1)
                # i만큼 밀어주고 1과 and 연산을 통해 제일 끝의 값만 남김
                bit_sum += (num >> i) & 1
            
            bit_sum %= 3    # 3의 나머지 연산을 통해 3번 중복된 애들은 0으로 변환. 유니크한 값은 1로 남게 됨 
            ans = ans | (bit_sum << i) # +, | 모두 작동
            
        if ans > 2**31 - 1:
            ans -= 2**32



        return ans
        
        """
        # num 개수만큼 카운팅하는 방법. O(n)의 추가 메모리를 사용하기에 문제에서 원하는 정답이 아님.
        dict_ = defaultdict(int)

        for num in nums:
            dict_[num] += 1
        
        for key, val in dict_.items():
            if val == 1:
                return key
        """
        