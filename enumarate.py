# How does enumerate work in Python? Enumerate functions much like a for loop, it loops over a
# collection of data once for each item in it. The primary difference is that enumerate also automatically modifies
# the data it is fed, essentially turning each item into a key-value pair. As the function iterates over the object,
# each item is paired with a number that corresponds to the number of times the loop has run including the current loop.
#
# The enumerate function accepts two parameters: the required iterable object, and the optional starting number. The
# starting number parameter accepts an integer and designates what number the function should start counting at.
# Given that it is optional, the default starting number is always zero, much like the indexing of arrays.
#
# Let’s look at some examples of this, and see how the input is changed by examining the output.
my_list = ['apple', 'orange', 'pear', 'grape', 'guava', 'mango', 'lemon', 'malta']
my_string = 'HelloWorld'

# for x, element in enumerate(my_list):
#     print(x, element)

obj_1 = enumerate(my_list)

# When we run enumerate function on a collection, it returns an object type of enumerate object
print(type(obj_1))

# When we run print function on enumerate object it prints the address where to enumerate object is stored
print(obj_1)

# We can use for loop and enumerate do get some stuff done easily
for x, element in obj_1:
    print(f'{x} -----> {element}')

print('----------------------------')

# Enumerate object generally starts from 0, we can also start from a non-zero number
obj_2 = enumerate(my_list, start=3)
for x, element in obj_2:
    print(f'{x} -----> {element}')

print('----------------------------')

# Enumerate function can be run on any iterable object like String, we can also start from a non-zero counter
for x, element in enumerate(my_string, start=2):
    print(f'{x}  -----> {element}')
print('----------------------------')



