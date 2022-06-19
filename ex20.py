from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_line_n(line_count, f):
    f.seek(0)
    for i in range(line_count-1):
        f.readline()
    print(f"{line_count}   {f.readline()}")


current_file = open(input_file)

print("Lets print the whole file. Here it is: ")
print_line_n(3, current_file)
print_line_n(1, current_file)

current_file.close()
