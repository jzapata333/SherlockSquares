import math

def squares(a, b):

    squareA = math.ceil(math.sqrt(a))
    squareB = math.floor(math.sqrt(b))

    result = squareB - squareA + 1

    print(result)    
    return result
    

squares(3,9)
squares(17,24)
squares(1, 1000000000)


