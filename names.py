

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(arr):

    for name in students:
        print name["first_name"],name["last_name"]

names(students)


users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
 }


def names_2(arr):
    for title in arr:
        position = 0
        print title
        for person in arr[title]:
            position = position + 1
            firstName = person['first_name'].upper()
            lastName = person['last_name'].upper()
            length = len(firstName) + len(lastName)
            print "{} - {} {} - {}".format(position, firstName, lastName, length)

names_2(users)
