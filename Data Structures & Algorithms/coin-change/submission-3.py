class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_coins=[float('inf')]*(amount+1)
        if(amount==0):
            return 0
        if all(coin > amount for coin in coins):
                return -1
        
        for coin in coins:
            if(amount>=coin>0):
                dp_coins[coin]=1

        dp_coins[0]=0
        print(dp_coins)

        # next step is for dp
        for i in range(1, len(dp_coins)):
            for coin in coins:
                if(i-coin>=0):
                    dp_coins[i]=min(dp_coins[i], dp_coins[i-coin]+1)
        print(dp_coins)
        return dp_coins[-1] if (dp_coins[-1] !=float('inf')) else -1