# Functions

# this one is like argv
# #* tells the function to expect a variable number of arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1 :{arg1}\targ2:{arg2}")

print_two("Habib", "Hassan")
