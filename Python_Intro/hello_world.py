words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")

print words.replace("day","month",1)
# 1 is the max replacement that will be done

x = [2,54,-2,7,12,98]
min_value = min(x)
max_value = max(x)
print min_value, max_value

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0],x[-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x

y = x[:len(x)/2]
z = x[len(x)/2:]
print y,z

z.insert(0,y)
print z
