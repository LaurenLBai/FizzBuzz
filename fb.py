# Lauren Baichtal
# 2/27/2022

# (i+1) will print 1 to 100 inclusive (i) by itself would print 
# from 0 to 99

# for i in range(100):
#     print (i+1)

#  A better alternative to print these numbers would be using the
#  range (1,101) and avoid adding the 1

for i in range(1,101):
    print(i)

# now to print the multiples of 3
# we can do that by using the modulo (%) with 3 = remainder 0

for i in range(1,101):
    if i % 3 == 0:
        print (str(i) + ' is a multiple of 3')
    else:
        print(str(i))

# now we can write a conditional to differenciate between multiples
# of 3 and multiples of 5

for i in range(1,101):
    if i % 3 == 0:
        print (str(i) + ' is a multiple of 3')
    elif i % 5 == 0:
        print (str(i) + ' is a multiple of 5')
    else:
        print(str(i))
    
    # next we need to label the cases when the numbers are multiples
    # of both 3 and 5
    
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print (str(i) + ' is a multiple of 3 and 5')
    else:
        print(str(i))

# When putting all the cases together, order matters (I learned this by doing 
# it wrong first) the conditional for both cases needs to be placed first, or 
# else the other conditionals would trigger first and override the case for both

# now I'll put together all the cases and replace the strings with the words
# Fizz, Buzz and FizzBuzz

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')
    elif i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    else:
        print(str(i))

    