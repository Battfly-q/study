# copy()

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# list() 方法

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# 切片运算符 [:]
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# 链接列表
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# 逐一加到附加的列表

list1 = ["a","b","c"]
list2 = [1,2,6]
for x in list2:
    list1.append(x)

print(list1)

# extend() 方法，其目的是将元素从一个列表添加到另一个列表：

list1 = ["a", "b" , "c"]
list2 = [9, 2, 3]

list1.extend(list2)
print(list1)