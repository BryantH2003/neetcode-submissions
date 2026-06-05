class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # result = [0] * len(temperatures)
        # lastIncreaseIndx = len(temperatures) - 2
        # decreaseCounter = 0

        # last = temperatures[-1]
        # for i in range(len(temperatures)-2,-1,-1):
        #     if temperatures[i] < last:
        #         decreaseCounter += 1
        #         result[i] = decreaseCounter
        #     else:
        #         result[i] = lastIncreaseIndx - i
        #         lastIncreaseIndx = i
        #         decreaseCounter = 0

        #     last = temperatures[i]
        # return result

        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1):
            right = i + 1
            counter = 1
            while right < len(temperatures):
                if temperatures[right] > temperatures[i]:
                    result[i] = counter
                    break
                else:
                    counter += 1
                
                right += 1
        
        return result
