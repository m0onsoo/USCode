# https://leetcode.com/problems/candy/
# 135-candy


class Solution:
    # def candy(self, ratings: List[int]) -> int:
    #     l = 0

    #     canides = [0] * len(ratings)
    #     prev_rating = -1
    #     prev_candies = 0

    #     for r, rating in ratings:
    #         if rating > prev_rating:
    #             prev_candies += 1
    #             candies[r] = prev_candies
    #         else:
    #             if prev_candies == 1:

    #             prev_candies = 1
    #             candies[r] = prev_candies
    #             l = r
    def candy(self, ratings: List[int]) -> int:
        prev = 0
        updown = [0] * len(ratings)
        for r, rating in enumerate(ratings):
            if rating > prev:
                updown[r] = 1
            elif rating == prev:
                updown[r] = 0
            else:
                updown[r] = -1
            prev = rating

        cont_zeros = [0] * (len(ratings) + 1)
        for i in range(len(ratings) - 1, -1, -1):
            if updown[i] == 0:
                cont_zeros[i] = cont_zeros[i + 1]
            elif updown[i] == -1:
                cont_zeros[i] = cont_zeros[i + 1] + 1

        candies = [0] * len(ratings)
        prev_candy = 0
        for i, status in enumerate(updown):
            if cont_zeros[i] == 0:  # 증가
                candies[i] = max(prev_candy + 1, cont_zeros[i + 1] + 1)
            else:
                candies[i] = cont_zeros[i]
            prev_candy = candies[i]

        print(updown)
        print(cont_zeros)
        print(candies)

        return sum(candies)


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        # [수정 1] prev 변수 대신 i와 i-1 직접 비교 (가장 안전)
        updown = [0] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                updown[i] = 1
            elif ratings[i] == ratings[i - 1]:
                updown[i] = 0
            else:
                updown[i] = -1

        # [수정 2] updown(왼쪽정보) 대신 ratings를 직접 보고 오른쪽 압력 계산
        # cont_zeros 이름을 그대로 썼지만, 의미는 '오른쪽 기준 최소 사탕 개수'로 맞춤
        cont_zeros = [1] * n
        for i in range(n - 2, -1, -1):
            # 내 점수가 오른쪽보다 높으면, 오른쪽 애보다 +1개 더 필요
            if ratings[i] > ratings[i + 1]:
                cont_zeros[i] = cont_zeros[i + 1] + 1
            # (아니면 기본값 1 유지)

        candies = [0] * n
        prev_candy = 0  # 이전 사람이 '왼쪽 규칙으로만' 받은 사탕 수

        for i, status in enumerate(updown):
            # [수정 3] 왼쪽 조건(left_run) 계산
            left_run = 1
            if i > 0 and updown[i] == 1:
                left_run = prev_candy + 1

            # 최종 결정: 왼쪽 조건 vs 오른쪽 조건(cont_zeros) 중 큰 값
            candies[i] = max(left_run, cont_zeros[i])

            # 다음 턴을 위해 '왼쪽 규칙 값'만 넘김 (max된 값 넘기면 안됨)
            prev_candy = left_run

        return sum(candies)
