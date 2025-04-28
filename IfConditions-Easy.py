num = int(input("Enter a number: "))
#this variable will tell the user to input a number
if (num % 2) == 0:
   print("{0} is an EVEN number".format(num))
#A number is even if division by 2 gives a remainder of 0 - the remainder has to be a whole number
else:
   print("{0} is an ODD number".format(num))
#If the remainder is 1, it is an odd number. - if the remainder given is not a whole number, it is not an even number

