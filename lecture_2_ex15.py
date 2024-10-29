#学习txt.read（）和open（）
"""from sys import argv

script,filename = argv

txt = open(filename)

print(f"here's your file {filename}")
print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again=open(file_again)

print(txt_again.read())"""


from sys import argv
script,filename= argv

txt = open(filename)

print(txt.read())

txt_again=open(input("please type your file again"))
print(txt_again.read())

print(txt_again.readline())