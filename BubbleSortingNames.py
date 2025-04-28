userName = ["Andreo","Lucas","Sydney","Zoe","Lisa","Jennie"]
#Create a variable which states the list in random order
numItems = 6
#Create a variable stating the number of names within the list
while numItems>1:
    for count in range(5):
        if userName[count] > userName[count+1]:
            temp = userName[count] 
            userName[count] = userName[count+1] 
            userName[count+1] = temp
    numItems = numItems-1

#print the outcome after everything is sorted
print(userName)
