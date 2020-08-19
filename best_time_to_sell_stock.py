#PROBLEM best time to sell stock 
def testFun():
    assert maxProfit([7,1,5,3,6,4]) == 5, "Function failed should be 5"

def maxProfit(prices:List[int])->int:
    cur_profit = max_profit = 0 
    start = prices[0]
    n = len(prices)

    for i in range(1,n):
        if prices[i] > start:
            #cur_profit = i-start
            #print(i, "cur profit", cur_profit)
            max_profit = max(prices[i]-start,max_profit)
            print(i, "max profit", max_profit)
        if prices[i] < start and prices[i] < min(prices[:i]):
            start = prices[i]
    return max_profit

