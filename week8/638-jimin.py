# https://leetcode.com/problems/shopping-offers/?envType=problem-list-v2&envId=dynamic-programming


# OPT[a,b,c,...] = minial total price of items when items quantity are a,b,c,...
# 너무너무 어려웠다... 사실상 포기
class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:

        OPT = defaultdict(int)

        def dfs(current_needs):
            if current_needs in OPT:
                return OPT[current_needs]

            # Base Case : use original price
            tot = 0
            for i in range(len(price)):
                tot += price[i] * current_needs[i]

            # Try to use Specia;
            for offer in special:
                flag = True
                new_need = list(current_needs)
                for i in range(len(needs)):
                    if current_needs[i] < offer[i]:
                        flag = False
                        break
                    new_need[i] -= offer[i]
                if flag:
                    tot = min(tot, dfs(tuple(new_need)) + offer[-1])
                # if flag and offer[-1] < tot:
                #     tot = dfs(tuple(new_need)) + offer[-1]

            OPT[current_needs] = tot
            return tot

        return dfs(tuple(needs))
