try:
    fh = open("ExceptionHandling.txt", "w")
    fh.write("Opening the file.\n")

    userInput = input("Enter any number: ")
    fh.write("The user entered number is: {}\n".format(userInput))

    result = 100 / int(userInput)
    fh.write("The final result is: {}\n".format(result))

    print("Result: ", result)
    # fh.write("Closing the file")
    # fh.close()
except ValueError:
    print("Please enter only numbers")
except ZeroDivisionError:
    print("Please enter numbers greater than zero.")
finally:
    fh.write("Closing the file")
    fh.close()