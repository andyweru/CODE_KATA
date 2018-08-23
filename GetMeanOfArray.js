export function getAverage(marks){
    //TODO : calculate the downwar rounded average of the marks array
    var sum = 0;
    for(let x = 0; x < marks.length; x++){
      sum += marks[x];
    }
    return Math.floor(sum/marks.length);
  }