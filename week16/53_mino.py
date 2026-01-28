n = len(arrays)
result = -10**4
for i in range(n):
  curr = 0
  for j in range(i+1, n+1):
    curr += arrays[j]
    if curr > result:
      result = curr

# How to make it O(N)?
# moving from left to right, keep a running sum
# If the sum is increasing, keep it
# Otherwise, update it with the final result 

# As you scan left to right, keep a running sum and reset it the moment it becomes worse than starting fresh at the current element.

# Scan left to right
for i in range(1, n):
  # keep a running sum
  curr += arrays[i]
  
  # if it becomes worse than starting fresh at the current element
  if curr < arrays[i]:
    # reset it
    curr = arrays[i]