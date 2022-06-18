#using several yield statement in a generator
def my_gen():
    n= 0
    print("This is the first statement")
    yield n

    n+= 1
    print("This is the second statement")
    yield n

    n+=1
    print("This is the third iterations")
    yield n

a= my_gen()#creating a genetator obj and it will not execute automatically
print(next(a))
print(next(a))
print(next(a))
#print(next(a)) stop iteration raised


#for loop with a generator
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)