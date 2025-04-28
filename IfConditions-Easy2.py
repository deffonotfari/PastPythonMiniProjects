inputname = input("Please enter your name: ")
#line 1 contains the variable which allows the user to input their name
print ("Thank you, " +inputname)
#this is a print statement. It is considered as a string which will print 'Thank you' and the user's name in the same line
inputNumber = input("Choose a number between 1 and 5: ")
#the user needs to input a number between 1 and 5 in order for the conditional variable to work
choice = int(inputNumber)
#this variable stores the number chosen by the user
if choice == 1:
  print (inputname + ", you really are quite brilliant!")
#if the user picks the number 1, it will display a message on the console
elif choice == 2:
  print (inputname +", you are quite intelligent")
#if the user picks the number 2, it will display a message on the console
elif choice == 3:
  print (inputname + ", you are wise!")
#if the user picks the number 3, it will display a message on the console
elif choice == 4:
  print(inputname + ", you really know what is right!")
#if the user picks the number 4, it will display a message on the console
elif choice == 5:
  print(inputname + ", you have a good luck")
#if the user picks the number 5, it will display a message on the console
else:
  print (inputname + ", you need to read the instructions carefully...you had to choose between 1 and 5")
#if the user picks a number which is above/below 1-5, it will tell the user to read the instructions carefully
