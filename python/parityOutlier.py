def find_outlier(integers):
    nums = integers
    even = []
    odd = []
    for num in nums:
        if(num%2 == 0):
            even.append(num)
        else:
            odd.append(num)
    if len(even) > len(odd):
        return odd[0]
    else:
        return even[0]