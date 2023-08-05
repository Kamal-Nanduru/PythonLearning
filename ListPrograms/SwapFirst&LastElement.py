# Python Program to swap first and last element of a list !

# Apporach 1 : 
# Swap function 
def swapList(newList):
    size = len(newList)

    # swapping
    temp = newList[0]
    newList[0] = newList[-1]
    newList[-1] = temp

    return newList

newList = [8, 4, 2]
print(swapList(newList)) 
# // [2, 4, 8]


# Apporach 2 : 
# The last element of the list can be referred as list[-1]. 
# Therefore, we can simply swap list[0] with list[-1].

def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList

newList = [8, 4, 2]
print(swapList(newList))

#Apporach 3 : 
# Swap the first and last element is using tuple variable. Store the first and last element as a pair in a tuple variable, say get, and unpack those elements with first and last element in that list. Now, the First and last values in that list are swapped. 
# Swap function
def swapList(list):
    # Storing the first and last element
    # as a pair in a tuple variable get
    get = list[-1], list[0]
     
    # unpacking those elements
    list[0], list[-1] = get
     
    return list
     
# Driver code
newList = [8, 4, 2]
print(swapList(newList))

# Apporach 4 : 
# Using * operand. 
# This operand proposes a change to iterable unpacking syntax, 
# allowing to specify a “catch-all” name which will be assigned a list of all items not assigned to a “regular” name. 
# the usage of * operand
# Swap function
def swapList(list):
     
    start, *middle, end = list
    list = [end, *middle, start]
     
    return list
     
# Driver code
newList = [8, 4, 2]
 
print(swapList(newList))

# Apporach 5 :
# Swap the first and last elements is to use the inbuilt function list.pop(). 
# Pop the first element and store it in a variable. 
# Similarly, pop the last element and store it in another variable. 
# Now insert the two popped element at each other’s original position. 

# Swap function
def swapList(list):
     
    first = list.pop(0)  
    last = list.pop(-1)
     
    list.insert(0, last) 
    list.append(first)  
     
    return list
     
# Driver code
newList = [8, 4, 2]
print(swapList(newList))

#  Approach #6: Using slicing
# In this approach, we first check if the list has at least 2 elements.
# If the list has at least 2 elements, 
# we swap the first and last elements using slicing by assigning the value of the last element to the first element and the value of the first element to the last element.
# We then slice the list from the second element to the second-to-last element and concatenate it with a list containing the first element and the last element in their new positions.
def swap_first_last_3(lst):
    # Check if list has at least 2 elements
    if len(lst) >= 2:
        # Swap the first and last elements using slicing
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst
 
# Initializing the input
inp=[8, 4, 2]
 
# Printing the original input
print("The original input is:",inp)
 
result=swap_first_last_3(inp)
 
# Printing the result
print("The output after swap first and last is:",result)