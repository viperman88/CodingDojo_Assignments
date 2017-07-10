
''' Write a function that simulates tossing a coin 5,000 times.
Your function should print how many times the head/tail appears.
Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you! '''

import random

def coin_toss(end):

    tails = []
    heads = []
    attempt = []

    print "Starting the program..."

    for i in range(0,end):
        random_num = random.randint(0,1)

        if random_num is 0:
            tails.append(1)
            attempt.append(1)
            print ("Attempt #{}".format(sum(attempt)) + " Throwing a coin... It's a tails!... Got {}".format(sum(tails)) + " tail(s) so far and {}".format(sum(heads)) + " head(s) so far")

        else:
            heads.append(1)
            attempt.append(1)
            print ("Attempt #{}".format(sum(attempt)) + " Throwing a coin... It's a heads!... Got {}".format(sum(heads)) + " head(s) so far and {}".format(sum(tails)) + " tail(s) so far")

    print "Ending the program, Thanks!"

coin_toss(20)
