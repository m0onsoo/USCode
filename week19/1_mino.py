# Given 
# an array of integers
# integer - target

# Goal
# return indices of the two numbers in the array such that they add up to targer

# Constaints
# Assume that there is only one index pair
# array.length <= N
# The same element cannot be used twice
# No extra memory usage or O(N)
# Elements in the array and target can be negative

# Example
# [1,2,3,10] -> 11: [0,3]

# Observations
# Find exactly two numbers that can add up to target
# If we don't match two numbers, we need to store the numbers temporarily

# Approach
# there should be a data structure to store the first index and temporary sum -> HashMap
# Initialize a hashmap to store elements
# Iterate through the array:
# target - array[i] is used as a key, value is the first element's index
# If the second number is found to add up to the target, break the loop
# return the indices of the numbers

# Input: integer array, integer
# Output: integer array

# TC: O(N)
# SC: O(N)

def twoSum(arrays:List[int], target:int) -> List[int]:
  index_map  = dict()
  answer = None
  
  
  for i in range(len(arrays)):
    remaining_diff = target - arrays[i]
    if remaining_diff in index_map:
      answer = [index_map[target-arrays[i]], i]
      break
      
    index_map[arrays[i]] = i
    
    
	return answer