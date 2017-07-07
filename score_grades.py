import random

def grades(total):

    for i in range (0, total):
        random_num = random.randint(60,101)

        if random_num <= 69:
            print "score:", random_num, "your grade is a D"

        elif random_num > 69 and random_num <= 79:
            print "score:", random_num, "your grade is a C"

        elif random_num > 79 and random_num <= 89:
            print "score:", random_num, "your grade is a B"

        elif random_num > 89 and random_num <= 100:
            print "score:", random_num, "your grade is a A"

    print "end of program, BYE!!"

grades(10)
