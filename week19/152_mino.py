# Given
# integer array

# Goal
# find a subarray that has the largest product

# Constraints
# array.length <= N
# -10 <= array[i] <= 10

# Example
# [1,2,3,4] -> [0,3]:24
# [1,2,3,-4] -> [0,2]:12
# [-1,2,3,-4] -> [0,3]:24
# [2,-3,-4,5]

# Observation
# record the largest product from each starting index 
# If we can use a data structure, 
# How to find a subarray? O(N^2)
# For each index, find the other index that produces the largest product

# Approach
# Brute-force
# Initialize global product and global indices to keep track of the largest product and its start and end index
# iterate through the array
# For each index:
# initialize the temp_product, index with the smallest integer value and 0
# keep multiplying each element in the array
# if the current product is greater than the temp_product,
# update the temp_product and index

# Hint
# When you multiply by a number, the “best so far” can flip if the number is negative.
# So at position i, tracking only the maximum product ending at i isn’t enough—also track the minimum product ending at i (because a very negative value times a negative can become the new max).
# Also decide what to do when you hit 0 (it cleanly “breaks” a running product).

# Approach
# min_product
# max_product
# store min and max product at each i
# reset if I hit 0:
# 1. if any product result is negative, the product result would be reset to 0
# 2. if any product result is positive, update it
# 3. 
# product_results = [(0,0)]


def maxProduct(self, nums: List[int]) -> int:
  start_index, end_index = 0, 0
  global_product = -float("inf")
  
  for i in range(len(nums)):
    temp_product = 1
    for j in range(i, len(nums)):
      temp_product *= nums[j]
      if temp_product > global_product:
        start_index = i
        end_index = j
        
	return [i,j]

def maxProduct(self, nums: List[int]) -> int:
  min_results = [float("inf")] * len(nums)
  max_results = [-float("inf")] * len(nums)
  
  min_end, max_end = nums[0], nums[0]
  for i in range(1, len(nums)):
      
    min_end = min(nums[i], min_end * nums[i])
    max_end = max(nums[i], max_end * nums[i])
    
		if min_end > max_end:
      temp = max_end
      min_end = max_end
      max_end = min_end

    max_results[i] = max_end
    min_results[i] = min_end

    
        
	return max(max_results)


def maxProduct(self, nums: List[int]) -> int:
  answer = -float("inf")
  prev_max, prev_min = nums[0], nums[0]
  for i in range(1, len(nums)):
    if nums[i] < 0:
      prev_min, prev_max = prev_max, prev_min
      
		prev_min = min(nums[i], prev_min * nums[i])
    prev_max = max(nums[i], prev_max * nums[i])
    
    answer = max(answer, prev_max)
        