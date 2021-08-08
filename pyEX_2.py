try:
    userInput = input("Enter any number: ")
    result = 100 / int(userInput)
    print("Result: ", result)
except ValueError:
    print("Please enter only numbers")
except ZeroDivisionError:
    print("Please enter numbers greater than zero.")
except Exception as e:
    print("Some exception occurred.", e, e.__class__)