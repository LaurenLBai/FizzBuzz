# Lauren Baichtal
# 2/24/2022

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
    if i% 3 == 0:
        print (str(i) + ' is a multiple of 3')

# now we can write a conditional to differenciate between multiples
# of 3 and multiples of 5

for i in range(1,100):
    if i % 3 == 0:
        print (str(i) + ' is a multiple of 3')
    elif i % 5 == 0:
        print (str(i) + ' is a multiple of 5')
    else:
        print(str(i))
    
    # next we need to label the cases when the numbers are multiples
    # of both 3 and 5
    
    