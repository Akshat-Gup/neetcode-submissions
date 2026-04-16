class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            sorted_letters = sorted(string)
            if str(sorted_letters) in groups:
                groups[str(sorted_letters)].append(string)
            else:
                groups[str(sorted_letters)] = [string]
        return list(groups.values())