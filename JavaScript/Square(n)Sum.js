function squareSum(numbers){
    var sum = 0;
    for(let x = 0; x < numbers.length; x++){
      sum += numbers[x]*numbers[x];
    }
    return sum;
  }