# Lab 04 : Data Structures

#  Question 4:

# a.
# They could use a list object to store the prices and map these prices to items within a dictionary
# eg.
# dict = { item_1 : [price_1, price_2, ...], item_2 : [price_1, price_2], ...}


# b.



some_list_of_floats = [ 1.2, 1.4, 1.5, 1.6, 1.7 ]       # original list

length_of_list = len(some_list_of_floats)               # determine the number of items in the original list

new_float = 1.6                                         # new float to be inserted

def binary_insert(new_float, some_list_of_floats):      # function definition
    index = 0
    while index < (length_of_list) - 1:                 # loop until last digit within the original list has been tested


        # if a position if found where the new float can be inserted between items in the original list, insert and break
        if some_list_of_floats[index] <= new_float <= some_list_of_floats[index + 1]:
            some_list_of_floats.insert( (index + 1), new_float )
            break
        index += 1
    if( length_of_list == len(some_list_of_floats) ):  # check if an insertion has been done
      
        if some_list_of_floats[0] > new_float:          # if no insertion has been done yet and the new float is smaller than
                                                        # the first item in the original list, add the new float to the beginning
            some_list_of_floats.insert( 0, new_float)
        
        else:                                           # if no insertion has been done yet and the new float is greater than
                                                        # the last item in the list, append the new float to the list
            some_list_of_floats.append( new_float )
        
    print some_list_of_floats                           # print the new list
    
    return
    
binary_insert(new_float, some_list_of_floats)


