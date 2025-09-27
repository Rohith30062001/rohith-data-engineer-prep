# 4. Find Missing Number

# Problem: Given n numbers in range [0, n], find the missing one.
# Solution:

def missing_number(nums):
    n = len(nums)
    return n * (n+1) // 2 - sum(nums)

print(missing_number([3,0,1]))  # 2

