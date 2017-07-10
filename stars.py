
#Create a function called draw_stars() that takes a list of numbers and prints out *.

one = [3,7,12,5,9]
two = [9,3,9,10,6]
three = [14,2,9,3,7]

def drawStarsOne(arr):
    for i in arr:
        print "*" * i

drawStarsOne(one)



four = ["Hello",6,"World",3,"Coding",10]
five = ["Yo Yo Yo",20,12,"What's","up"]

def drawStarsTwo(arr):

    for x in arr:
        if isinstance(x,str):
            idx = x[0].lower()
            print idx * len(x)

        if isinstance(x,int):
            print "*" * x

drawStarsTwo(five)
