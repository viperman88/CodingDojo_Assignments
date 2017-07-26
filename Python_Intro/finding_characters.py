word_list = ['hello','world','my','name','is','Robert']
char = 'o'

#Write a program that takes a list of strings and a string containing a
#single character, and prints a new list of all the strings containing that character.


words_with_o = []

for str in word_list:
	if str.find(char) != -1:
		words_with_o.append(str)

print words_with_o
