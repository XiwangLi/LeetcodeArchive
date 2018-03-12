class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
# This smaller size problem for DR:
# find out min (DP[amount - coin]) + 1 for coin in coins
        Max = float('inf')
        DP = [Max] * (amount + 1)
        DP[0] = 0
        for i in xrange(1, len(DP)):
            for coin in coins:
                if i - coin < 0:
                    continue
                else:
                    DP[i] = min (DP[i], DP[i - coin] + 1)  # the induction rule
        return DP[amount] if DP[amount] != Max else -1
        

# this problem can also be solved using DFS
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse = True)
        Max = float('inf')
        res = [Max]
        for i in range(len(coins)):
            self.dfs(i, amount, 0, res, coins)
        return res[0] if res[0] < Max else -1
        
    def dfs(self, idx, rem, count, res, coins):
        if not rem:
            res[0] = min(res[0], count)
            return
        for i in range(idx, len(coins)):
            if coins[i] <= rem < coins[i] * (res[0] - count): 
                self.dfs(i, rem - coins[i], count + 1, res, coins)