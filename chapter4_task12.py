def myDecorator(func):
    def wrapper(*args, **kwargs):
        print("Calling testFunc:", args, kwargs)
        func(*args, **kwargs)

    return wrapper

@myDecorator
def testFunc(a, b=1, *args, **kwargs):
    print("argument a: ", a)
    print("argument b: ", b)
    print("argument args: ", args)
    print("argument kwargs: ", kwargs)
    print("Finished testFunc", a+b)


testFunc(1,2,3,4, c=6, d=7)
print()
testFunc(1, c=6)