# Binary Search
def binary_search(arr, target):
  """
  Performs a binary search on a sorted array.

  Args:
    arr: The sorted array to search.
    target: The value to search for.

  Returns:
    The index of the target value if found, otherwise -1.
  """
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = left + (right - left) // 2  # [1] Avoid overflow using this formula for calculating mid

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1  # [2] Search the right half
    else:
      right = mid - 1  # [2] Search the left half

  return -1  # Target not found

# A test case
print(binary_search([1,2,3,4,5,6,7],6))
