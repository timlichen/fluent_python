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

# symbols = '&#$((@(#$*)))'
# # print tuple(ord(symbol) for symbol in symbols)
#
# import array
# # print array.array('I', (ord(symbol) for symbol in symbols))
#
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
#
#
# for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
#     print tshirt
#
# for tshirt in [(color, size) for color in colors for size in sizes]:
#     print tshirt

# The key difference here is that the generator expression feeds the for loop producing one item at a time. If the two lists used in the Cartesian produt had 1000 items each, using the generator expression would save the expense of building a list with a million items just to feed it into the loop.

# Tuples as Records
fmt = '{:15} | {:^9.4f} |   {:^9.4f}'
metro_areas = [
    ('Tokyo','JP', 36.933, (35.689722, 139.691667)),
    ('Dehli NCR','IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
]

# for name, cc, pop, (latidute, longitude) in metro_areas:
#     if longitude <= 0:
#         print(fmt.format(name, latidute, longitude))

# https://docs.python.org/3.5/library/string.html#formatspec

# Defining and using a named tuple

# Instances of classes built with named tuples take exactly the same amount of memory as tuples because the field names are stored in the class. They use less memory than a regular object because they don't store attributes in a per-instance dict.


from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
# tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)
# print(tokyo.population)
# print(tokyo.coordinates)
# print[tokyo[1]]

City._fields # _fields is a tuple with the field nmes of the class
LatLong = namedtuple('LatLong', 'lat long')
dehli_data = ('Dehli NCR','IN', 21.935, LatLong(28.613889, 77.208889))

delhi = City._make(dehli_data) # _make() allow you to instatiate a named tuple from an iterable; City(*delhi_data) would do the same.

# print delhi._asdict() # returns collections.OrderedDict built froom the named tuple instance. That can be used to produce a nice display of city data.

# for key, value in delhi._asdict().items():
    # print(key + ":", value)

# Tuple as immutable lists.

# Tuples support all list methods except those that add or remove, one exception to this rule is the lack of __reversed__ support. This is just for optimiation reversed(my_tuple) works without it.

# Slice!

# seq.__getitem__(slice(start, stop, step))

s = 'bicycle'
# print(s[::3])
# print (s[::1]) # 1 step
# print (s[::-1]) # 1 step - reversed
# print (s[::2])
# print (s[::-2]) # remove

l = list(range(10))
# print(l)

l[2:5] = [20,30]
# print(l)

del l[5:7]
# print(l)

l[3::2] = [11,12]
# print(l)

# When the target of the assignment is a slice, the right side must be an iterable object, even if it's just one item.

my_sub_list = ["a"]
# print(hex(id(my_sub_list)))
my_list = [my_sub_list]
operated_list = my_list * 3

# print(hex(id(operated_list[1]))) # internal lists referece all reference to the same list.

# operated_list[1][0] = "zzz" # this changes the value for all lists since they are all referenced to the same list.
# print operated_list

# Building a list of lists

board = [['_'] * 3 for i in range(3)] # right

# board = []
# for i in range(3):
    # row = ['_'] * 3
    # board.append(row)

# print(board)
board[1][2] = '0'
# print(board)

weird_board = [['_'] * 3] * 3 # wrong

# row = ['_']
# board = []
# for i in range(3):
#     board.append(row)

# print(weird_board)
weird_board[1][2] = '0'
# print(weird_board)

# A += assignment puzzler...
# t = (1,2,[30, 40])
# t[2] += [50, 60]
# print(t)

# In python shell, this code results in a tuple object does not support item assignment, but the list at t[2] still gets modified. You can modify this with t[2].extend[50, 60] to make the change without an error

# putting mutable items in tuples is not a good idea.
# augmented assignment is not an atomic operation -- we just saw it throwing it an excepton after doing part of the job.
# inspecting Python bytecode is not too difficut, and is often helpful to see what is going on under the hood.


################################################################################
# This is a great tool to use with students to help breakdown and explain code!
# http://pythontutor.com/visualize.html#mode=edit
################################################################################

fruits = ["grapes", "strawberries", "oranges", "apples"]
print sorted(fruits)
print sorted(fruits, key=len, reverse=True)
print fruits # sorted is not done in place, but return a new list.
print fruits.sort() # python convention is for methods are operate in place to return None
print fruits
