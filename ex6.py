types_of_people = 10
# inserts types_of_people variable into string using format
x = f"There are {types_of_people} types of people"

# format string to be assigned to y with the variables binary and do_not
binary = 'binary'
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

# assign boolean value False to hilarious
hilarious = True

# assigns formattable string to joke_evalutaion, {} makes it formattable using the method str.format()
joke_evaluation = "Isn't that joke so funny?! {}"

# prints the result of formatting joke_evalutation with value stored in the variable hilarious
print(joke_evaluation.format(hilarious))

w = "This is the left side..."
e = " of a string with a right side"

# print the string that results from concatenating w and e
print(w + e)
