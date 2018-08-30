import math

def two_decimal_places(number):
  if number < 0:
    return (math.ceil(number*100)/100)
  else:
    return (math.floor(number*100)/100)