# Author: Kayla Robinson, 06/06/2025

# TASK 1: create a function that takes the input: list of integers, e.g. [8, 3, 5, 1] and returns 8351 (an int)
# Approach:
#       need to get the len of the list
#       need to get each individual element of the list in order
#       use 10^len to get the biggest, then iterate down with len-i to get each successive digit
#       can then sum the to get the entire number

def list_to_int(number: list) -> int: # input is of type list, and we are returning an int
    
    length = len(number)
    total = 0 # initialise the total before the for loop

    for i in range(length): # number = [8, 3, 5, 1]
        digit = number[i] # otherwise could use an index that increases
        # digit = 8
        # print(digit) used to check that we are in fact returning the correct digit

        place = 10**(length - i - 1)
        # print(place) used to check that it was to the correct power {saw that we got 4, 3, 2, 1 --> used -1 to generate correct powers}

        total = total + (digit*place)

    return total

inp1 = [8,3,5,1]
print(list_to_int(inp1))

inp2 = [3,4,6,2,5,7,8,9]
print(list_to_int(inp2))