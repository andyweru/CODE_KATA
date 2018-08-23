function digitize(numbers) {
    //code here
    var myArray = numbers.toString().split("").reverse();
    return myArray.map(x => parseInt(x))
  }