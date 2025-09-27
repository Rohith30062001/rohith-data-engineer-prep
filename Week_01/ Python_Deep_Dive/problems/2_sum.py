# 1. Two Sum (LeetCode Easy)

# Problem: Given an array of integers, return indices of the two numbers that add up to a target.
# Solution:


arr = [1,2,3,4,5,9]
sum = 10

for ele in arr:
    if (sum-ele) in arr:
        print(ele, sum-ele)


# [2,7,11,15], 9  # [0, 1]
sum = 9
arr = [2,7,11,15]
for i in range(len(arr)-1):
    for j in range(i, len(arr)):
        if arr[i]+arr[j] == sum:
            print(i,j)
        