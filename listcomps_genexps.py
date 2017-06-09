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

for key, value in delhi._asdict().items():
    print(key + ":", value)
