class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = []
        words = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord("z") - ord(c)] += 1
            words[tuple(count)].append(word)


        ans = []
        for val in words.values():
            ans.append(val)

        return ans



        