import sys

def karatsuba(x, y):
    # Base case for recursion: if either number is smaller than 10,
    # simply return the product (handles single-digit multiplication).
    if x < 10 or y < 10:
        return x * y
    
    # Determine the size of the numbers.
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    
    # Split the digit sequences at the half point.
    high_x = x // (10 ** half) #a
    low_x =  x % (10 ** half)  #b
    high_y = y // (10 ** half) #c
    low_y =  y % (10 ** half)  #d
    
    # 3 recursive calls of Karatsuba.
    ac = karatsuba(high_x, high_y)
    bd = karatsuba(low_x, low_y)
    ab_cd = karatsuba((high_x + low_x),(high_y + low_y))
    
    #Karatsuba's formula.
    return (((10 ** (2 * half))*ac) + ((10 ** (half)) * ((ab_cd-bd-ac)) + bd))

#Inputs for Karatsuba
x = 1
y = 1

#Perform Karatsuba
result = karatsuba(x, y)

#Print the result
print("Result:", result)


#check
#if x * y == result:
 #   print('you got it')

#else:
 #   print('wrong')
sys.exit
