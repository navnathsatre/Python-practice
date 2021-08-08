import re

s = "purple alice@google.com abcde helloab@abc.com ---@gmail.com 23@gmail.com my23@gmail.com _@gmail.com"

emails = re.findall(r"\w+@\w+\.\w+", s)
print(emails)

emails = re.findall(r"[A-Za-z]\w+@\w+\.\w+", s)
print(emails)