import myModule

import tkinter

print("myMain's __name__    : ", __name__)
print("myModule's __name__  : ", myModule.__name__)

# Two executions
# 1. Run myMain.py
# myMain.py -> __name__    -> __main__
# myModule.py -> __name__  -> myModule

# 2. Run myModule.py
# myModule.py -> __name__ -> __main__