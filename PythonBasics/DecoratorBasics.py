# A decorator takes in a function, adds some functionality and returns it.
# In this program, you will learn how you can create a decorator
# and why you should use it.
#
# One way to do it
def simple():
    print("I am a simple function")

def decoratorFunction(func):
    def innerFunction():
        print("I am decorating something on simple")
        func()
    return innerFunction

#decoratorFunction(simple)



def anotherDecorator1(func):
    def innFunc():
        print("I am another decorator to check the twice decorating ")
        func()
    return innFunc()

# Anothere way by using @ annotation


@anotherDecorator1
def simple1():
    print("i am another simple function")