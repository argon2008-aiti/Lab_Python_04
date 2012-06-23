# Lab 04:  Data Structures

# Question 4 c

groceries = [ 'bananas', 'strawberries', 'apples', 'champagne' ]          # sample grocery list

items_to_price_dict = { 'apples': [ 1.1, 1.3, 3.1 ], 'bananas': [ 2.1, 1.4, 1.6, 4.2 ],  
                            'oranges': [ 2.2, 4.3, 1.7, 2.1, 4.2 ],                       # different prices of items on the market
                            'pineapples': [ 2.2, 1.95, 2.5 ], 'champagne': [ 6.5, 5.9 ],      
                            'strawberries': [ 0.98, 1.1, 0.67, 0.99 ] }

def min_cost( grocery_list, item_to_price_list_dict ):    # function to determine the minimum cost of the grocery items

    total_min_cost = 0   # current total of minimum cost of grocery items                        

    for item in grocery_list:    # iterate over the grocery list
        if item in item_to_price_list_dict:  # test if the current grocery list item is contained in the prices list dictionary
            total_min_cost = total_min_cost + min(item_to_price_list_dict[item]) # get the minimum price of the current grocery list item and add that
                                                                                 # to the current total of minimum cost
    print " The minimum cost is: ", total_min_cost  # print the total minimum cost 



min_cost( groceries, items_to_price_dict ) # test the function with the values provided


