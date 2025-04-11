# 没有推导列表

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# 列表推导式
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
# for x in fruits: 遍历fruits列表中的每一个元素x
# if "a" in x : 检查当前元素x 是否包含字母:"a"
# [x ...]:如果满足条件，就将x加入新列表

# 等效
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)  

newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in fruits]

print(newlist)