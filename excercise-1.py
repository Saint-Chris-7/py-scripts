
#the function will create a generator object
def infinite():
    num= 0
    while True:
        yield num
        num +=4

gen=infinite()
print(next(gen))

#instead of using a for loop you can use next() since
#for loop will execute automatically
for i in infinite():
    print(i)