# sort()
# 


# 按字母排序
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# 按数字排序
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#降序排序 reverse = True
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# 自定义排序功能 key = function
def myfunc(n):
#   abs()内置函数，返回一个数的绝对值（无论正负都会变成非负数）。
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# 区别大小写
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# 逆序
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
