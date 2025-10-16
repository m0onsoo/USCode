from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # OPT(i): min number of coins to make amount i
        # OPT(i) = min(OPT(i), min([OPT(i-k)+1 for k in coins]))

        # initialize opt array with maximum number (amount + 1)
        opt = [amount + 1] * (amount + 1)
        opt[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    # if amount is larger than coin, update opt[i] with min number of coins to make amount i (if impossible, it still remains (amount+1))
                    opt[i] = min(opt[i], opt[i-coin] + 1)

        if opt[-1] == amount+1:
            # if we can't make amount, return -1
            return -1
        return opt[-1]