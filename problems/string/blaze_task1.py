
class Solution:

    def get_split_charecter(self, s):
        unique_set = set(s)
        res = []
        for s1 in unique_set:
            if s.count(s1) >1 and s1 not in res:
                res.append(s1)
        return res

    def get_unicque_substring_count(self, s):
        unique_set = self.get_split_charecter(s)
        print("unique_set", unique_set)
        data = []
        for s1 in unique_set:
            print("s1", s1)
            data.extend([ s1 + e1 for e1 in s.split(s1) if e1])
        r1 = set(data)
        print(r1)
        res = len(r1)
        return res

# Task1:(Python) to split the string into the maximum number of unique substrings and
# return count of it.
# Split only at occurance of character that repeats else output is string length itself.

if __name__ == '__main__':
    obj = Solution()
    # ip1 = "cycle"
    ip1 = "ababccc"
    print(obj.get_unicque_substring_count(ip1))