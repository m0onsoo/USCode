# https://leetcode.com/problems/3sum/
# 15-3sum

# Brute force -> n^3
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         ans_set = set()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         temp_set = tuple(sorted((nums[i], nums[j], nums[k])))
#                         if temp_set not in ans_set:
#                             ans_set.add(temp_set)
#                             ans.append(list(temp_set))

#         return ans

# Optimized
# What if I store every combination of 2 nums? -> n^2
# and then search for the complement in the hash map. -> n

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         pairs = defaultdict(list)   # sum -> list of (i, j) with i < j < current k
#         triplets = set()            # dedupe: store sorted tuples

#         for k in range(n):
#             need = -nums[k]
#             if need in pairs:
#                 for i, j in pairs[need]:
#                     if j < k:  # 같은 원소 재사용 방지
#                         trip = tuple(sorted((nums[i], nums[j], nums[k])))
#                         triplets.add(trip)

#             # k를 오른쪽 끝으로 하는 모든 쌍 (i, k)를 추가
#             for i in range(k):
#                 s = nums[i] + nums[k]
#                 pairs[s].append((i, k))

# return [list(t) for t in triplets]


# Optimized Pointer
## store pairs sum.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # i 중복 제거

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # l, r 중복 스킵
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return res
