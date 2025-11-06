from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        n = len(price)
        # memo: DP 테이블 역할을 할 딕셔너리
        # Key: 튜플(needs), Value: 최소 비용
        memo = {}

        def solve(current_needs: Tuple[int]) -> int:
            
            # --- 1. 기저 사례 (Base Case) ---
            # 모든 아이템이 0개 필요하면 비용은 0
            if all(n == 0 for n in current_needs):
                return 0

            # --- 2. 메모이제이션 확인 ---
            # 이미 이 상태를 계산했다면 저장된 값을 반환
            if current_needs in memo:
                return memo[current_needs]

            # --- 3. 옵션 1: 스페셜 오퍼 없이, 모두 개별 구매 ---
            # 이 비용을 최소 비용의 초기값으로 설정
            min_cost = 0
            for i in range(n):
                min_cost += current_needs[i] * price[i]

            # --- 4. 옵션 2: 모든 스페셜 오퍼를 시도 ---
            for offer in special:
                offer_price = offer[n]
                next_needs = list(current_needs) # 다음 재귀로 넘길 '남은 needs'
                is_offer_usable = True

                # 이 오퍼를 현재 needs로 살 수 있는지 확인
                for i in range(n):
                    if current_needs[i] < offer[i]:
                        is_offer_usable = False # 아이템이 부족해서 오퍼 사용 불가
                        break
                    # 오퍼를 사용하고 남은 아이템 개수
                    next_needs[i] = current_needs[i] - offer[i]

                # 오퍼를 사용할 수 있다면, 재귀 호출
                if is_offer_usable:
                    # (오퍼 가격) + (오퍼 적용 후 남은 아이템을 사는 최소 비용)
                    cost_with_offer = offer_price + solve(tuple(next_needs))
                    
                    # (개별 구매) vs (오퍼 사용) 중 더 싼 값으로 갱신
                    min_cost = min(min_cost, cost_with_offer)

            # --- 5. 결과 저장 및 반환 ---
            memo[current_needs] = min_cost
            return min_cost

        # ---
        # 최초 호출: needs 리스트를 튜플로 변환하여 시작
        # ---
        return solve(tuple(needs))
        
        """
        #  bottom up approach
        n, m = len(needs), max(needs)
        dp = [[0] * (m+1) for _ in range(n+1)]

        # print(dp)
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i][j-1] + price[i-1]
        
        # print(dp)
        need_prc = 0
        for i, need in enumerate(needs):
            need_prc += need * price[i]
        # need_prc = sum(dp[i, need]) # i번째 아이템의 need개 만큼의 합
        # print(need_prc)

        for offer in special:
            disc_prc, flag = 0, 0
            for i, _ in enumerate(zip(needs, offer[:-1])):
                need, off_num = _[0], _[1]
                # print(i+1, need, off_num)

                if need >= off_num:
                    flag = 1
                    disc_prc += dp[i+1][need - off_num]
                else:
                    # 하나라도 만족하지 않을 시 즉시 종료
                    flag = 0
                    break
            if flag:
                disc_prc += offer[-1]
                need_prc = min(need_prc, disc_prc)

                # dp테이블도 갱신 필요


        return need_prc
        """