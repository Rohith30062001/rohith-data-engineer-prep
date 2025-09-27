# 5. Move Zeroes

# Problem: Move all zeroes in array to the end, maintaining order of non-zero elements.
# Solution:

li = [0,1,0,3,12]

new_li = []
zeroes = []
for ele in li:
    if ele !=0:
        new_li.append(ele)
    else:
        zeroes.append(0)

new_li = new_li+zeroes
print(new_li)
