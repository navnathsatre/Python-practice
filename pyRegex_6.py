import re
sampleString = '''
Rohit made 122 runs, Virat made 96 runs, and
Dhawan made 46 runs and we won the match.
'''

# {"Rohit": 122, "Virat": 96, "Dhawan": 46}
lstNames  = re.findall(r"[A-Z][a-z]+", sampleString)
lstScores = re.findall(r"\d+", sampleString)

print("Names : ", lstNames)
print("Scores: ", lstScores)

# Approach 1
# result = {}
# for item in range(3):
#     result[lstNames[item]] = lstScores[item]
#
# print(result)

# Approach 2 : Zip
print(dict(zip(lstNames, lstScores)))