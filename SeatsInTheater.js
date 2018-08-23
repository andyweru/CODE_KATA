function seatsInTheater(nCols, nRows, col, row) {
    //coding and coding..
    
  //   number of people seated behind me(but same column)
    var sameCol = nRows - row;
    
  //   number of people on my left (including my row)
    var sameRow = nCols - col+1;
    
  //   return total people begind me and on my left
    return sameCol * sameRow;
    
  }