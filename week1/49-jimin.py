# https://leetcode.com/problems/group-anagrams/
# 49-group-anagrams.py
# Ideas :
# 1. Naive (Brute Force)
# - compare each element with each other element.
# - O(n*m^2) where n is len(strs), m is len(strs[i])
# 2. Use hash set
# - turn all elements into a set
# - compare the sets . if an anagram is found, save it into an array
# - if comparison is complete for the element, save the array to res array
# - also check for found ones.

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result = []
#         sets = []
#         check_found = {}
#         for string in strs:
#             sets.append(Counter(string))
#         for i, string in enumerate(sets):
#             temp_arr = []
#             if i not in check_found:
#                 temp_arr.append(strs[i])
#                 for j in range(i + 1, len(sets)):
#                     if sets[i] == sets[j] and j not in check_found:
#                         temp_arr.append(strs[j])
#                         check_found[i] = True
#                         check_found[j] = True
#                 result.append(temp_arr)
#         return result


# 3. Sort -> defaultDict (basically a list that can append to a non-existing key)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))  # 핵심: sorted
            groups[key].append(s)  # 핵심: defaultdict
        return list(groups.values())
