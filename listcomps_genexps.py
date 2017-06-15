# LIST COMPREHENSION
################################################################################

# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# tshirts = [(color, size) for color in colors for size in sizes]
#
# print tshirts # cartesian product from list comprehension

# Same thing can be achieved with nested loops
# for color in colors:
#     for size in sizes:
#         print(color, size)

################################################################################
# Generator Expressions
################################################################################

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

################################################################################
# Tuples as Records
################################################################################

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

################################################################################
# Defining and using a named tuple
################################################################################

'''
Instances of classes built with named tuples take exactly the same amount of memory as tuples because the field names are stored in the class. They use less memory than a regular object because they don't store attributes in a per-instance dict.
'''

'''
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print[tokyo[1]]
'''

# City._fields # _fields is a tuple with the field nmes of the class
# LatLong = namedtuple('LatLong', 'lat long')
# dehli_data = ('Dehli NCR','IN', 21.935, LatLong(28.613889, 77.208889))

# delhi = City._make(dehli_data) # _make() allow you to instatiate a named tuple from an iterable; City(*delhi_data) would do the same.

# print delhi._asdict() # returns collections.OrderedDict built froom the named tuple instance. That can be used to produce a nice display of city data.

# for key, value in delhi._asdict().items():
    # print(key + ":", value)

################################################################################
# Tuple as immutable lists.
################################################################################

'''
Tuples support all list methods except those that add or remove, one exception to this rule is the lack of __reversed__ support. This is just for optimiation reversed(my_tuple) works without it.
'''

################################################################################
# Slice!
################################################################################

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

''' When the target of the assignment is a slice, the right side must be an iterable object, even if it's just one item. '''

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

'''
# In python shell, this code results in a tuple object does not support item assignment, but the list at t[2] still gets modified. You can modify this with t[2].extend[50, 60] to make the change without an error

# putting mutable items in tuples is not a good idea.
# augmented assignment is not an atomic operation -- we just saw it throwing it an excepton after doing part of the job.
# inspecting Python bytecode is not too difficut, and is often helpful to see what is going on under the hood.

################################################################################
# This is a great tool to use with students to help breakdown and explain code!
# http://pythontutor.com/visualize.html#mode=edit
################################################################################
'''
################################################################################
# Sorting lists and arrays
################################################################################

# fruits = ["grapes", "strawberries", "oranges", "apples"]
# print sorted(fruits)
# print sorted(fruits, key=len, reverse=True)
# print fruits # sorted is not done in place, but return a new list.
# print fruits.sort() # python convention is for methods are operate in place to return None
# print fruits

################################################################################
# Managing ordered sequences with bisect.
################################################################################
# bisect does a binary search, which must be performed on a sorted sequence.

import bisect
import sys

HAYSTACK = [1,4,5,6,8,12,15,20,21,23,23,26,29,30]
NEEDLES = [0,1,2,5,8,10,22,23,29,30,31]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:2<d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle) # Use the chosen bisect function to get the insertion point.
        offset = position * '  | ' # build a pattern of vertical bars proportional to the offset.
        print(ROW_FMT.format(needle, position, offset)) # print formatted row showing needle and insertion point

if __name__ == '__main__':
    if sys.argv[-1] == 'left': # choose the bisect function to use according to the last command-line argument
        bisect_fn = bisect.bisect_left # python 3 this_file.py left
    else:
        bisect_fn = bisect.bisect

# print('DEMO: ', bisect_fn.__name__) # print header with name of function selected
# print('hk ->',  '  '.join('%2d' % n for n in HAYSTACK))
# demo(bisect_fn)

# Table lookups by numeric values -- for example, to convert test scores to letter grades.

def grade(score, breakpoints = [60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

# print [grade(score) for score in [33,99,77,70,89,90,100]]

################################################################################
# Inserting with bisect.insort
################################################################################

# import random
# SIZE = 7
# random.seed(1729)
# my_list = []
# for i in range(SIZE):
#     new_item = random.randrange(SIZE*2)
#     bisect.insort(my_list, new_item)
#     print('%2d -> ' % new_item, my_list)

'''
If you need to store 10 million floating-point digits, lists might not be the best option, an array would be much more efficient, this is because and array does not actually hold full-fledged float objects, but only the packed bytes representing their machine values, on the other hand, if your constantly adding and removing items from the ends of a list as a FIFO data structure, a deque (double ended queue) works faster.
'''

################################################################################
# Creating, saving, and loading a large array of floats.
################################################################################

# from array import array # import array type
# from random import random
#
# floats = array('d', (random() for i in range(10**7))) # create an array of double precision floats (typecode 'd') from any iterable object -- in this case, a generator expression
# print(floats[-1]) # inspect the last number in the array
# fp = open('floats.bin', 'wb')
# floats.tofile(fp) # save the array to a binary file
# fp.close()
# floats2 = array('d') # create an empty array of doubles
# fp = open('floats.bin', 'rb')
# floats2.fromfile(fp, 10**7) # read 10 million numbers from the binary file
# fp.close()
#
# print(floats2[-1]) # inspect the last number in the array
#
# print(floats2 == floats)

################################################################################
# Memory Views
################################################################################

'''
A memoryview is essntiall a generalized NumPy array structure in Python itself (without the math). It allows you to sare memory between data-structures (things like PIL images, SQLite databases, NumPy arrays, etc.) without first copying. This is very important for larger data sets.
'''
################################################################################
# Changing the value of an array item by poking one of its bytes
################################################################################

# import array
# numbers = array.array('h', [-257, -1, 32767, 1, 2])
# memv = memoryview(numbers) # building mem-view from signed integers, typecode 'h' ( signed short 2-byte minimum )
# # print(len(memv))
# # print(memv[0]) # memv sees the same 5 elements.
#
# memv_oct = memv.cast('B') # casting elements of memv to typecode 'B', ( unsigned char in C Python int type 1-byte minimum )
#
# print(memv_oct.tolist()) # export to list for inspection
# # print("here", memv_oct[0])
#
# # memv_oct[4] = 0
# memv_oct[0] = 4 # assign value 4 to byte offset 5.
# print(memv_oct.tolist())
#
# print(numbers) # A 4 in the most significant byte (octet) of a 2-byte unsigned integer is 1024.

import numpy
''' Basic opetions with rows and columns in numpy.ndarray '''
a = numpy.arange(12)
print(a)
type(a)
print(a.shape)

a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])
print(a[:, 1]) # get column at index 1
print(a.transpose()) # create a new array b transposing (swapping columns with rows).
