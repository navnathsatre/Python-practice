nums = range(1, 11)

print("Numbers: ", nums)

even = lambda n: n % 2 == 0


def isEven(n):
    return n % 2 == 0

print(even(5))
print(even(10))

filterObj = filter(even, nums)
print("Result using filter - even: ", list(filterObj))

mobj = map(even, nums)
print("Result using map - even: ", list(mobj))