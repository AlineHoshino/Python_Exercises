from sys import argv 

script = argv

print("Type the file:")
file_again = input('>')

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
