# 3. Anagram Check

# Problem: Check if two strings are anagrams.
# Solution:

str1 = "silent"
str2 = "listen"
anagram = False


if set(list(str1))==set(list(str2)):
    print('anagram')