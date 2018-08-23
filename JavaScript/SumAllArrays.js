function arraySum(arr) {
    // sum ALL the things!
  
    
    //  function for adding elements in array
    var sum = 0;
    for(var i = 0; i < arr.length; i++){
        //  Add element with sub elements
        if(arr[i].length > 1){
          sum += arraySum(arr[i]);
        } else{
              if(typeof arr[i] == "number"){
                  sum += arr[i];
              }
        }
    }
    
    return sum;
  }