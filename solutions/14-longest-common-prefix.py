class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''

        shortest_length = min(map(lambda x: len(x), strs))
        for i in range(shortest_length):
            criteria = strs[0][i]

            for s in strs:
                if s[i] != criteria:
                    return common_prefix
            common_prefix += criteria
        
        return common_prefix
