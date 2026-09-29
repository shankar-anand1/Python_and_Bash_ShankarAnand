# Write to a file

f = open("notes.txt", "w")
f.write("DevOps assignment - file handling\n")
f.write("This file was created using open() and write().\n")
f.write("Student: Shankar Anand\n")
f.close()
print("File notes.txt created.")
