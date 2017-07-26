var money = 0.01
var days = 30
for(var i = 1; i <= days; i++){
    if(i <= days){
        console.log(money);
        money = money * 2
    }
}

function howMuchMoney(money,days){
    for(var i = 1; i <= days; i++){
        if(i <= days){
            console.log(money);
            money = money * 2
        }
    }
}
howMuchMoney(0.01,30)

/*
30 days you would earn $5,368,709.12
21 days you break $10,000
38 days to break 1 billion
1032 days to reach infinity
*/
