def validate_pin(pin):
    #return true or false
      if pin.isdigit() and pin >= 0:
        if len(pin) == 4 or len(pin) == 6:
            return True 
        return False
      return False