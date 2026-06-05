class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        sortedMap = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            print(sortedWord)
            if sortedWord in sortedMap:
                sortedMap[sortedWord].append(word)
            else:
                sortedMap[sortedWord] = [word]
        
        for key in sortedMap:
            result.append(sortedMap[key])

        return result