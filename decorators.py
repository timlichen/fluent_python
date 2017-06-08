# Python Decorators

def classmethod(funk):
    print "funky!", funk # the foo function has been passed in
    def inner_func(arg1, arg2): # the inner function accepts arguments
        shmoo1 = arg1
        shmoo2 = arg2
        for i in range(8):
            shmoo1 += 1
            shmoo2 += 2
            funk(shmoo1, shmoo2) # this inner function is capable of executing the foo method, meta
    return inner_func # the inner_func must be returned so that it can be called again?

@classmethod
def foo (arg1, arg2):
    print 'arg1', arg1
    print 'arg2', arg2

foo(1,2)

# The above code is eq. to foo = classmethod(innerfunc(foo))
# By decorating the foo function with the sugar @classmethod, the foo function is passed into the classmethod function as a parameter and altered without actually having to change the foo method.
