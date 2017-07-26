function numRange(start,end,skip){
    for(i = start; i < end; i = i + skip){
        if(skip === undefined){
            skip = 1;
        }
            {
            console.log(i);
            }
    }
}

numRange(-10,10,2)
