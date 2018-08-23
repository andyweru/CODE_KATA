// Smash Words
function smash (words) {
    "use strict";  
    
    if(words.length == 1){
      return words[0];
    } else {
      var result = ""
      for(let x = 0; x < words.length; x++){
        result += ` ${words[x]}`;
      }
    }
    
    return result.slice(1);
};