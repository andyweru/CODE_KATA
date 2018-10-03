def str_count(strng, letter):
    # Your code here ;)
    number = 0
    for char in strng:
        if char == letter:
            number += 1
            
    return number