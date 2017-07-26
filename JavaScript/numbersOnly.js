
function numbersOnly(arr){
    var newArray = [];

    for(var i = 0; i < arr.length; i ++){
        if(typeof arr[i] === "number"){
        newArray.push(arr[i]);
        }
    }
    console.log(newArray);
}
numbersOnly([1, "apple", -3, "orange", 0.5, 22, "hello", 6])

//Second function that removes them

function numbersOnly(arr){

    for(var i = 0; i < arr.length; i++){
        if(typeof arr[i] === "string"){
        arr.splice(i,1);
        }
    }
    console.log(arr);
}
numbersOnly([1, "apple", -3, "orange", 0.5, 22, "hello", 6])
