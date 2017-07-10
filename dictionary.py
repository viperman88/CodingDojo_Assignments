
info = {
"Name":"Robert Amato",
"Age":"35",
"Country of origin":"USA",
"Favorite language":"Python",
}


def personal_info():

    for key,data in info.iteritems():

        print "My",key,"is",data
        #print "My " + key + " is " + data   #<-Can also be written like this 

personal_info()
