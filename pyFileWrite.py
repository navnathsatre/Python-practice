# w => Write Mode
# r => Read Mode
# a => Append Mode

fh = open("FileExample.txt", "w")
print("FH Object    : ", fh)
print("type of fh   : ", type(fh))

fh.write("Welcome to file handling in Python.\n")
fh.write("This is second line.\n")
fh.write("Always close the file once the job is done.\n")

fh.close()
