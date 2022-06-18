#generator expression use parenthesis
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)


#getting items from the list
print(next(generator))
print(next(generator))
print(next(generator))


#represent an infinte stream of data like an endless data
def all_even():
    n = 0
    while True:
        yield n
        n += 2


#piplining a series of data. 
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))