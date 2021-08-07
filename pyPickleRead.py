import pickle

fh = open("vdStates", "rb") # rb -> read + binary

contents = pickle.load(fh)

fh.close()

print("File contents: ", contents)
print("type of file contents: ", type(contents))

# Marshal - Unmarshal
# Serialization - Deserialization
# COM - DCOM