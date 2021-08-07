from functools import reduce

nums = range(1, 11)

print("Numbers: ", nums)

myfunc = lambda x, y: x + y

print(myfunc(7,8))

result = reduce(myfunc, nums)
print("Result using reduce: ", result)