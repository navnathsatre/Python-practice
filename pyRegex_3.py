import re
address = "78 Hi 11    89 Main, 4th Cross, 123, Road, Marathalli, 5678 Bangalore, 560023 67893"

lstValues = re.findall(r"\d+", address)
print("Numbers using the pattern '\d+'      : ", lstValues)

lstValues = re.findall(r"\d{6}", address)
print("Numbers using the pattern '\d{6}'      : ", lstValues)

lstValues = re.findall(r"\d{2}", address)
print("Numbers using the pattern '\d{2}'      : ", lstValues)

lstValues = re.findall(r"\s?\d{2}\s", address)
print("Numbers using the pattern '\s?\d{2}\s'      : ", lstValues)

lstValues = re.findall(r"\d{1,6}", address)
print("Numbers using the pattern '\d{1,6}'      : ", lstValues)