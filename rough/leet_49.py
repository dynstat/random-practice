class Solution:
    def groupAnagrams(self, strs):
        answer_dict = {}

        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord("a")] += 1
            try:
                answer_dict[tuple(counts)].append(s)
            except:
                answer_dict[tuple(counts)] = [s]

        # print(answer_dict.values())
        return list(answer_dict.values())


if __name__ == "__main__":
    sol_obj = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol_obj.groupAnagrams(strs)
