# 1. Print all ints from 0 t0 150:
for i in range(1, 151):
    print(i)
# range used for printing a range of numbers, in this case 1 to 150.
# 2. Print all the multiples of 5 from 5 to 1,000:
# 3. Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo":
multiples = []
for i in range(5, 5001):
    if i % 5 == 0:
        multiples.append(i)
print(multiples)
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
for z in range(1, 101):
    if z % 5 == 0:
        print("Coding")
    if z % 10 == 0:
        print("CodingDojo")
    else:
        print(z)
# if/else statement to replace N value with string of chocie.
# 4.Add odd integers from 0 to 500,000, and print the final sum:
result = 0
for x in range(1, 500001):
    if (x % 2 == 1):
        result = result+x
print("Sum of Odd Numbers Using for loop = ", result)
# When adding a String AND Variable make sure to keep them seperated so Python knows it's a Variable not part of a String or List.
# 5. Countdown by fours:
for c in range(2017, 1, -4):
    if (c % 2 == 1):
        # Exculdes odd numbers BECAUSE when run, Python sees that those numbers have a remander and therefore can't be an even number.
        c += 1
        print(c)
#6. # Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9.
lowNum = 2
highNum = 9
mult = 3

for f in range(lowNum, highNum + 1):
    if f % mult == 0:
        print(f)
