def odd_even(start,end):

    for i in range (start,end):
        if (i % 2 == 1):
            print "Number is: {}.".format(i) + " This number is odd."
        if (i % 2 == 0):
            print "Number is: {}.".format(i) + " This number is even."

odd_even(1,20)



def multiply(arr,num):

    for i in range(0,len(arr)):
        arr[i] = arr[i] * num
    return arr

array = [2,4,6,8,10,22,44,66,88,100]

print multiply(array,5)



def layered_multiples(arr):
  # your code here
  
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
