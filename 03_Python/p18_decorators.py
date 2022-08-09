#Creates a function that gets another function f as input often called decorator
def announce(f):
    #Creates a function that calls the function f inside of it
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

#Adds the decorator to this function and pass the function as input at announce() function then the function wrapper
#prints the About message, and then runs the function on the input f => functionHello()
@announce
def functionHello():
    print("Hello world function")

#Calls function functionHello()
functionHello()

#Adds the decorator to this another function as well
@announce
def functionNotHello():
    print("Not saying Hello to the world function")

#Calls function functionHello()
functionNotHello()