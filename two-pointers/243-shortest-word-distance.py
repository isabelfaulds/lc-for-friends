class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 , w2 = -1 , -1
        min_distance = float('inf')

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1 = i
            if wordsDict[i] == word2:
                w2 = i
            if w1 != -1 and w2 != -1:
                distance = abs(w1 - w2)
                min_distance = min(distance, min_distance)

        return min_distance