# fh = open("FileExample.txt", "r")
fh = open("FileExample.txt")

strContents = fh.read()
fh.close()

print("File Contents: ", strContents)