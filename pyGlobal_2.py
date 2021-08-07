def myFunction():
    global temp
    temp = "Global Python Object"
    print("Value of temp: ", temp)
    print("Inside myFunction")


myFunction()
print("The value of temp in global scope:", temp)