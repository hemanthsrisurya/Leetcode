class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrank = numBottles
        empty = numBottles
        while empty >= numExchange:
            newBottles = empty // numExchange
            totalDrank += newBottles
            empty = empty % numExchange + newBottles
        return totalDrank
