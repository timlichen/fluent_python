# http://jeffknupp.com/blog/2013/11/29/improve-your-python-decorators-explained/

# def counterAbove31(innerfunction):
#   def checker(a,b):
#     if counter < 31:
#       return "Counter not high enough"
#     else:
#       return innerfunction(a,b)
#   return checker
#
# def add(a,b):
#   print (a + b)
#
# functionStore = counterAbove31(add)
# counter = 29
# print functionStore(12,45)
# counter = 100
# functionStore(12,45)

# def is_even(value):
#     return (value % 2) == 0
#
# def count_occurances(target_list, predicate):
#     return sum([1 for e in target_list if predicate(e)])
#
# my_predicate = is_even
# my_list = [2,4,6,7,9,11]
#
# result = count_occurances(my_list, my_predicate)
# print(result)

def surround_with(surrounding):
    def surround_with_value(word):
        # {} are positional arguments .. https://docs.python.org/2/library/string.html
        return '{}{}{}'.format(surrounding, word, surrounding)
    return surround_with_value

def transform_words(content, targets, transform):
    result = ''
    for word in content.split():
        if word in targets:
            result += ' {}'.format(transform(word))
        else:
            result += ' {}'.format(word)
    return result

markdown_string = 'My name is Tim Chen and I like Python'
markdown_string_ital = transform_words(markdown_string, ['Python', 'Tim'], surround_with('*'))
# print (markdown_string_ital)

string = ['This', 'is', 'a', 'string']
surround1 = "cat"
surround2 = "dog"
surround3 = "tim"

print '{} {} {}'.format(surround1, string[0], surround3)
