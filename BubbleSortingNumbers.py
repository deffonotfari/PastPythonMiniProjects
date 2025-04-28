def bubble_sort(list):
#run loops two times: one for walking throught the list and the other for comparison


    n = len(list) 
    swapped = True 
    print(myList)
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if list[i - 1] > list[i]:
                #swap both values
                temp = list[i-1]
                list[i-1] = list[i]
                list[i] = temp
                swapped = True
        
        print(list)        
                    
myList = [6, 5, 4, 3, 2, 1] #this variable holds the list
bubble_sort(myList) #the program will now carry out the action after it is defined
