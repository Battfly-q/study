# mylist = ["1","2","3"]
# print(len(mylist))
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(type(list1))
# print(list2)
# print(list3)
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist[-2])
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
# thislist = ["apple", "banana", "cherry"]
# thislist[0] = "11"


# in的作用
# if "apple" in thislist:
   
#   print("Yes, 'apple' is in the fruits list")
# else:
#   print("no")

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# append 最后一位
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# 扩展 extend extend()方法不必附加列表，
# 您可以添加任何可迭代对象（元组、集合、字典等）。
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

#remove()移除制定目标
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# 如果有多个具有指定值的项目，该remove()方法将删除第一个出现的项目：
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# pop()方法删除指定的索引。
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# 如果不指定索引，该pop()方法将删除最后一项
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#  del关键字还删除指定的索引：
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# del关键字还可以彻底删除列表。
thislist = ["apple", "banana", "cherry"]
del thislist

# clear()清空列表。
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#  循环遍历列表
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#range()和 len()函数来创建合适的可迭代对象
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
