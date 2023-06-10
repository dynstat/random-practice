class Solution:
    out = []
    orig = []
    orig2 = []

    def str_match(self, s1, s2):
        for ch in s1:
            if ch in s2:
                continue
            else:
                return False
        self.orig2.remove(s1)
        return True

    # def check_anag(self, in_set):
    #     while True:
    #         try:
    #             string = yield
    #             if string == "-1":
    #                 print("stopping generator")
    #                 break
    #             inner_list = []
    #             str_len = len(string)
    #             for s in in_set:
    #                 if len(s) != str_len:
    #                     continue
    #                 else:
    #                     r = self.str_match(s, string)
    #                     if r:
    #                         inner_list.append(s)
    #             yield inner_list
    #         except Exception as e:
    #             yield inner_list

    def groupAnagrams(self, strs):
        self.orig = list(set(strs))
        self.orig2 = self.orig.copy()

        # anagen = self.check_anag(self.orig2)
        # next(anagen)
        while True:
            if self.orig2:
                to_match = self.orig2.pop(0)

                self.out.append([to_match])
                for i in self.orig2:
                    if self.str_match(i, to_match) and i not in self.out[-1]:
                        self.out[-1].append(i)
            else:
                break
        print(self.out)


if __name__ == "__main__":
    sol_obj = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol_obj.groupAnagrams(strs)
