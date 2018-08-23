function find_average(array) {
    // your code here
    var sum = 0;
    for(let x = 0; x < array.length; x++){
      sum += array[x];
    }
    return sum/array.length;
  }