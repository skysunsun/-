from sys import argv

script, filename = argv

txt = open(filename)#打开文件

print(f"Here's your file {filename}:")
print(txt.read())#读文件

print("Type the filename again:")
file_again = input(">")#手动输入

txt_again = open(file_again)#打开文件

print(txt_again.read())#读文件
