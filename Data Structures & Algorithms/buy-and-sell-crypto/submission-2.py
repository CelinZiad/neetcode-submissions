class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        min_index = 0
        max_index = 1
        current_profit = prices[max_index] - prices[min_index]
        max_profit = current_profit
        for i in range (1, len(prices)):
            print(f"i: {i}")
            current_profit = prices[max_index] - prices[min_index]
            print(f"current profit: {current_profit}")
            print(f"min index: {min_index}")
            print(f"max index: {max_index}")
            print(f"buy: {prices[min_index]}")
            print(f"sell: {prices[max_index]}")
            if prices[min_index] > prices[max_index]:
                min_index = max_index
                max_index += 1
                print(f"min index: {min_index}")
                print(f"max index: {max_index}")
            elif prices[min_index] <= prices[max_index]:
                max_profit = max(current_profit, max_profit)
                max_index +=1
        
        if max_profit>0:
            return max_profit
        return 0
        """
        min = prices[0]
        max = prices[1]
        if min>max:
            min = max
            max = min+1
        if min<max
        """