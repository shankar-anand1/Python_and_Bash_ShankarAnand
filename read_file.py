# Read from a file

f = open("notes.txt", "r")
content = f.read()
f.close()
print("File content:")
print(content)
