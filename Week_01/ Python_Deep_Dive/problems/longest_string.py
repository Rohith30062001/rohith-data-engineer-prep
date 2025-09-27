# 2. Longest Substring Without Repeating Characters (Medium)

# Problem: Find the length of the longest substring without repeating characters.

string = "abcabcbb"  # 3 ("abc")
largest = ""
current = ""

for i in range(len(string)):
    if string[i] not in current:
        current+=string[i]
    elif string[i] in current and len(current)>len(largest):
        largest = current
        current = ""

print(largest, len(largest))

