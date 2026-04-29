class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        if len(hand) % groupSize:
            return False

        totalGroups = len(hand) // groupSize

        count = Counter(hand)
        hand.sort()
        curMax = 0
        curGroups = 0
        # 1 2 2 3 3 4 4 5
        for num in hand:
            if count[num] <= 0:
                continue
            for i in range(num, num + groupSize):
                print(num, i)
                if i not in count:
                    return False
                else:
                    count[i] -= 1
                    if count[i] < 0:
                        return False
            
            curGroups += 1
            if curGroups == totalGroups:
                return True

        return False