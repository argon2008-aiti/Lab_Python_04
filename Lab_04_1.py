#LAB 04: Data Structures

# Question 1


groceries = [ 'bananas', 'strawberries', 'apples', 'bread' ]
print groceries
print
print

# a.

# to add champagne to the 'groceries' list
print "added champagne"
groceries.append('champagne')
print groceries
print
print

# b.

# to remove bread from the 'groceries' list
print "removed bread"
groceries.remove('bread')
print groceries
print
print

# c.

# in order to make it easy for John to find the items he needs, he must sort his list
n = 0
aisles = raw_input("Enter aisles( a - z ): ")
for item in groceries:
    if item.startswith(aisles):
        print "Items on this aisles :"
        n += 1
        print item,

if n == 0:
    print " This aisles does not contain any item you wish to buy!" 
