import re

print("Find all matches for format Month day")
matches = re.findall(r"[A-Z][a-z]+\s\d{1,2}", "These are the match dates June 24, August 9, Dec 12")
print(matches)

matches = re.findall(r"([A-Z][a-z]+)\s\d{1,2}", "These are the match dates June 24, August 9, Dec 12, and Nov")
print(matches) #only months

matches = re.findall(r"[A-Z][a-z]+\s(\d{1,2})", "These are the match dates June 24, August 9, Dec 12")
print(matches) # only day

matches = re.findall(r"([A-Z][a-z]+)\s(\d{1,2})", "These are the match dates June 24, August 9, Dec 12")
print(matches) # In Tuple Formate