from sys import argv
script,filename = argv

file = open(filename)
file_read = file.read()

print(f"The file's name is \"{filename}\"\nthe content of the file is:\n{file_read}")


