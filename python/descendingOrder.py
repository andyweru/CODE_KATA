def Descending_Order(num):
    #Bust a move right here
    List = [int(x) for x in str(num)]
    sortedList = sorted(List, reverse = True)
    stringified = [str(x) for x in sortedList]
    
    result = ''.join(stringified)
    return int(result)