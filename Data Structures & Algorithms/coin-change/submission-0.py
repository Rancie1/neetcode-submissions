class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float("inf")

            if rem in memo:
                return memo[rem]

            min_coins = float("inf")
            for coin in coins:
                res = dp(rem-coin)
                if res != float("inf"):
                    min_coins = min(res+1,min_coins)
            memo[rem] = min_coins
            return min_coins
        memo = {}
        if dp(amount) != float("inf"):
            return dp(amount)
        else:
            return -1
        