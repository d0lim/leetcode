class Solution:
    def hIndex(self, citations: List[int]) -> int:
        result = [0 for _ in range(5001)]
        for citation in citations:
            result[citation] += 1

        max_citation = max(citations)

        hIndex = 0
        for i in range(1, max_citation + 1):
            count = 0
            for j in range(i, max_citation + 1):
                count += result[j]
                if count >= i:
                    hIndex = max(hIndex, i)
                    count = 0
                    break

        return hIndex
