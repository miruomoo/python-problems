class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<r:
            x = numbers[r]+numbers[l]
            if x>target:
                r-=1
            elif x<target:
                l+=1
            else:
                return [l+1, r+1]