# Given
# integer array: nums
# integer k

# Goal
# find all the subarrays whose sum equals to k

# Constraints
# 1 <= N <= 2*10^4
# No extra constraints on memery usage

# Observations
# A subarray is a continguous non-empty sequence: nums[i:j]
# The longest subarray = array nums
# The smallest subarray = each element
# (1) At the start, expand the sub-array until the sum equals to or exceeds k
# If the sum equals to k, count up the current number of subarrays
# Move the starting point to the right and recalculate the sum
# Go to (1) and expand the sub array to the right again.

# TC: O(N)
# SC: O(1)

# Input / Output
# Input:
# - integer array: nums
# - integer: k

# Output:
# - integer

# Example
# [1,1,1], 2
# [1,2,3], k = 3

dfs findTheNumOfSubarrays(nums: List[int], k:int) -> int:
  l, r, n = 0, 0, len(nums)
  answer, current_sum = 0,0
  
  while l <= r:
    if l == n:
      break
    if r == n:
	    current_sum += nums[r] # 1, 3, 5
	    r += 1 # 1,2, 3
    
    # check if the sum equals to k
    if current_sum >= k: 
      if current_sum == k:
      	answer += 1 # 1
      current_sum -= nums[l] # 2, 3
      l += 1 # 1, 2
    
  return answer