

//First assignment

var students = [
    {first_name:  'Michael', last_name : 'Jordan'},
    {first_name : 'John', last_name : 'Rosales'},
    {first_name : 'Mark', last_name : 'Guillen'},
    {first_name : 'KB', last_name : 'Tonel'}
]

for(var i in students){
    console.log(students[i].first_name + " " + students[i].last_name);
}


//Second assignment, option 1, probably easier to understand if you did not write it

var users = {
 'students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

console.log("Students")

for(var i in users.students){
    var firstLength = users.students[i].first_name.length;
    var lastLength = users.students[i].last_name.length;
    var nameLength = firstLength + lastLength;
    console.log(i + "-" + users.students[i].first_name + " " + users.students[i].last_name + "-" + nameLength)
}

console.log("Instructors")

for(var i in users.instructors){
    var firstLength = users.instructors[i].first_name.length;
    var lastLength = users.instructors[i].last_name.length;
    var nameLength = firstLength + lastLength;
    console.log(i + "-" + users.instructors[i].first_name + " " + users.instructors[i].last_name + "-" + nameLength)
}


//Second assignment, second option, no variables for length written in console.log

var users = {
    'students': [
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
    ],
    'instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
    ]
 }

console.log("Students")

for(var i in users.students){
    console.log(i + "-" + users.students[i].first_name + " " + users.students[i].last_name + "-" + (users.students[i].first_name.length + users.students[i].last_name.length));
}

console.log("Instructors")

for(var i in users.instructors){
    console.log(i + "-" + users.instructors[i].first_name + " " + users.instructors[i].last_name + "-" + (users.instructors[i].first_name.length + users.instructors[i].last_name.length));
}
