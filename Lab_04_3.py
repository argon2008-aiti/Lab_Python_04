#LAB 04: Data Structures

# Question 3:

# a.
# the best data structure to use for displaying a list of foods in Shoprite is 'list' object

# b.

# create a list which contains all the food items at Shoprite

in_stock = [ 'Apples', 'Bananas', 'Bread', 'Carrots', 'Champagne' , 'Strawberies' ]
print in_stock
print

# c.

# a tuple is immutable and can therefor not change

always_in_stock = ('',)
for item in in_stock:
    always_in_stock = (item,) + always_in_stock[:]
    
# d.

# to print out the items in always_in_stock
print "Come to shoprite! We always sell: "
print
for item in always_in_stock:
    print item
    
  

