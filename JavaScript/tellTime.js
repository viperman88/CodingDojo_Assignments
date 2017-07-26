function tellTime(hour,min,period){

    if(hour == 8 && min == 50 && period == "AM"){
        console.log("It's almost 9 in the morning!")
    }
    else if(hour == 7 && min == 15 && period =="PM"){
        console.log("It's just after 7 in the evening!")
    }
    else{
        console.log("The exact time is " + hour + ":" + min + period + "!")
    }

}

tellTime(8,50,"AM")
tellTime(7,15,"PM")
tellTime(6,30,"AM")



var HOUR = 7;
var MIN = 32;
var PERIOD = "AM";

if(MIN > 30 && PERIOD == "PM"){
    console.log("It's " + HOUR + ":" + MIN + " in the evening, and it's almost the next hour!")
}
else if(MIN > 30 && PERIOD == "AM"){
    console.log("It's " + HOUR + ":" + MIN + " in the morning, and it's almost the next hour!")
}
else if(MIN < 30 && PERIOD == "PM"){
    console.log("It's " + HOUR + ":" + MIN + " in the evening, and it's just after the hour!")
}
else{
    console.log("It's " + HOUR + ":" + MIN + " in the morning, and it's just after the hour!")
}
