class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            # 부호 저장
            sign = -1
            x = abs(x)

        result = 0
        while x:
            # 자릿수 올려주고 일의 자리에 나머지 더해주기
            result *= 10
            result += x % 10

            x = x // 10
        
        if result > 2**31 - 1 or result < -2**31:
            # 31bit 벗어나면 return 0
            return 0

        return result * sign

            