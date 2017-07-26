a = ["Hey","Oh",32,12,"No",41]
b = [23,65,2,7,21,29]
c = ["My","Friends","At","Coding","Dojo"]


stuff = a

newStr = ' '.join(i for i in stuff if isinstance(i, str))

num = sum(i for i in stuff if isinstance(i, int) or isinstance(i, float))

print newStr

print num

if len(newStr) > 0 and num > 0:
   print("The array you entered is of mixed type")

elif len(newStr) > 0 and num == 0:
   print("The array you entered is of string type")

elif len(newStr) == 0 and num > 0:
   print("The array you entered is of integer type")
