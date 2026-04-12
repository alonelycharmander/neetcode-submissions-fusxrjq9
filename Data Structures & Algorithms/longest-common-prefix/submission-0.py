class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = ""
        index = 0
        flag = True
        while flag: 
            for i in range(1, len(strs)):
                if index >= len(strs[i]) or index >= len(strs[i-1]):
                    return res
                if strs[i][index] != strs[i-1][index]:
                    return res
            res += strs[i][index]
            index += 1 

        return res