# LIST COMPREHENSION

# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# tshirts = [(color, size) for color in colors for size in sizes]
#
# print tshirts # cartesian product from list comprehension

# Same thing can be achieved with nested loops
# for color in colors:
#     for size in sizes:
#         print(color, size)

# Generator Expressions

symbols = '&#$((@(#$*)))'
# print tuple(ord(symbol) for symbol in symbols)

import array
# print array.array('I', (ord(symbol) for symbol in symbols))

colors = ['black', 'white']
sizes = ['S', 'M', 'L']


for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    print tshirt

for tshirt in [(color, size) for color in colors for size in sizes]:
    print tshirt

# The key difference here is that the generator expression feeds the for loop producing one item at a time. If the two lists used in the Cartesian produt had 1000 items each, using the generator expression would save the expense of building a list with a million items just to feed it into the loop.
