def product(numbers):
    # Implement me! :)
    if numbers == []:
        return None
        
    if numbers == None:
        return None
        
    if len(numbers) == 1:
        return numbers[0]
    
    result = 1
    for num in numbers:
        result *= num
    
    return result