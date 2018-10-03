def find_short(s):
    # your code here
      splitlist = s.split(' ')
      shortest = splitlist[0]
      for word in splitlist:
          if len(word) < len(shortest):
              shortest = word
      
      return len(shortest)