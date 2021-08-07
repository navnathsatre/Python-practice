# Take a sequence of inputs (numbers) (which are comma separated) and
# calculate the sum

# Enter sequence of numbers: 1,2,3,4,5
# Result: 15
usrInput = input("Enter any sequence of numbers: ")
print("User Input: ", usrInput)

# Step1 : Convert to list
lstNums = usrInput.split(",")
print("List of Numbers: ", lstNums)

# Step 2: Convert each element of list(having strings) to another list (of numbers)
lstOfInts = []
for item in lstNums:
    lstOfInts.append(int(item))

print("list of numbers (int): ", lstOfInts)

print("Result: ", sum(lstOfInts))

# Approach 2: (using Maps)
nwListInts = list(map(int, usrInput.split(",")))
print("Result: ", sum(nwListInts))

# Approach 3:
print("Result: ", sum(list(map(int, (input("Enter sequence of numbers: ").split(","))))))