# https://leetcode.com/problems/coin-change-ii/description/
# 518-coin-change


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        coins.sort(reverse=True)

        def dfs(amt, max_coin):
            combinations = 0
            for i, coin in enumerate(coins):
                if max_coin < coin:
                    continue
                if amt < coin:
                    continue
                elif amt == coin:
                    combinations += 1
                elif amt > coin:
                    combinations += dfs(amt - coin, coin)
            return combinations

        ans = dfs(amount, float("inf"))

        return ans


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 1. 계산 결과를 저장할 메모장 (Memoization)
        memo = {}

        # 큰 코인부터 처리하면 트리의 깊이가 얕아져서 조금 더 빠릅니다.
        coins.sort(reverse=True)

        # max_coin 값 대신 '현재 인덱스(idx)'를 넘기는 것이 캐싱하기 더 좋습니다.
        def dfs(amt, idx):
            if amt == 0:
                return 1

            # 2. 이미 계산해본 상황(금액, 인덱스)이라면 저장된 값 리턴
            state = (amt, idx)
            if state in memo:
                return memo[state]

            combinations = 0
            # 3. Loop 최적화:
            # `if max_coin < coin: continue`와 같은 효과를 내기 위해
            # 아예 `range(idx, len(coins))`로 루프 범위를 좁힙니다.
            for i in range(idx, len(coins)):
                coin = coins[i]

                # 금액이 남았을 때만 재귀 호출
                if amt >= coin:
                    # 동전 개수 제한이 없으므로, 다음 재귀에서도 현재 코인(i)부터 쓸 수 있게 넘김
                    combinations += dfs(amt - coin, i)

            # 4. 결과 저장
            memo[state] = combinations
            return combinations

        return dfs(amount, 0)


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        DP = [0] * (amount + 1)
        DP[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                DP[i] += DP[i - coin]

        return DP[amount]
