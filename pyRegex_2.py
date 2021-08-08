# GREP -> Global Regular Expression Print
import re

s = "Welcome to   Regex    Programming   using   Python"
print("The value of s                   : ", s)

lstValues = re.split(r"\s", s)
print("Regex split using '\s'           : ", lstValues)

lstValues = re.split(r"\s+", s)
print("Regex split using '\s+'          : ", lstValues)

lstValues = re.split(r"s+", s)
print("Regex split using 's+'           : ", lstValues)

s = "Welcome to Regex Programming using Python"
lstValues = re.split(r"[a-f]", s)
print("Regex split using '[a-f]'        : ", lstValues)

lstValues = re.split(r"[a-f][l-n]", s)
# [a-f] -> a b c d e f
# [l-m] -> l m n
# al am an bl bm bn cl cm cn
# dl dm dn el em en fl fm fn
# W
# come to Regex Progr
# ming using Python
print("Regex split using '[a-f][l-n]    : ", lstValues)