
# Given
# an array of integers

# Goal
# find the largest rectangle area

# Constraints
# 1 <= array.length <= N\

# Observations
# find the maximum area where the height would be capped to the minimum integer of the subarray
# array[i] >= 0

# Example
# [2,1,5,6,2,3] -> 2, 2, 5, 
# keep the start index, height, and prev_area
# compare at each i
# start:
# 	index = 0
#		height = array[0]
#		prev_area = array[0]

# current_height = min(height, array[1])
# current_area = current_height * (i - index)

# 1. current_area vs current_height -> reset if current_height is greater
# 2. current_area vs prev_area -> continue if current_area is greater

# DP solution: store the best so far and keep track of local info until the previous element


    def largestRectangleArea(self, heights: List[int]) -> int:
        prev_index = 0
        prev_height = heights[0]
    
        answer = prev_height

        for i in range(1, len(heights)):
          if heights[i] >= prev_height:
            prev_height = heights[i]
          else:
            current_area = min(heights[prev_index:i]) * (i - prev_index)
            
            answer = max(answer, current_area)
            
            prev_index = i
            prev_height = heights[i]
            
            
        
        return answer

# Hint
# Keep a structure of bars whose heights are monotonic increasing as you scan left → right.
# When you see a height that breaks that increase (i.e., smaller), you should “close out” one or more previous heights (because their right boundary is now i-1).
# Each stored item needs enough info to recover its leftmost start after popping.

# Approach
# store the previous height at every bar
# compare the prev with the current height
# if not increasing, close out and calculate the area
	# store the starting bar into the stack
  # Once closed out, pop the top element
  # calculate the max area
  # put the current height and index into the stack 
# update the max area by comparing the area to the current max area
# After iteration, return the max area

# TC: O(N)
# SC: O(N)

    def largestRectangleArea(self, heights: List[int]) -> int:
      	start_index = -1  
      	prev_height = float("INF")
				max_area = -float("INF")    
        
        for i in range(len(heights)):
          if heights[i] >= prev_height:
            prev_height = heights[i]
            continue
          
          # close out
          current_area = (i - start_index) * start_height
          max_area = max(max_area, current_area)
          prev_height = heights[i]
          start_index = i

        
        return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            # close out rectangles that can't extend past i-1
            while stack and stack[-1][1] > h:
                prev_start, prev_h = stack.pop()
                max_area = max(max_area, prev_h * (i - prev_start))
                start = prev_start

            # keep stack increasing by height
            stack.append((start, h))

        # close out remaining rectangles to the end
        n = len(heights)
        while stack:
            start, h = stack.pop()
            max_area = max(max_area, h * (n - start))

        return max_area