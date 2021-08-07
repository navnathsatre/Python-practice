from functools import reduce

nums = range(1, 11)

print("Numbers: ", nums)

myfunc = lambda x, y: x * y

print(myfunc(7,8))


def Multiply2Nos(x, y):
    return x * y

result = reduce(Multiply2Nos, nums)
print("Result using reduce: ", result)

# Hadoop
# Map-Reduce
# WordCount
# 100 Files OR 1 File - 100 GB
# 100 Parts - 100 * 1 GB => 100 Systems ->
# {WordA: 1, WordB: 10, WordC: 100, ...}

