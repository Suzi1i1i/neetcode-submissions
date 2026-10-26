class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) 
        out = []
        for str in strs:
            str_sort = "".join(sorted(str))
            anagrams[str_sort].append(str)

        return list(anagrams.values())
        