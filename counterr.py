from collections import Counter

a= "aaaaaabbbbbbbbcccccccccddddd"
my_cont= Counter(a)
print(my_cont)
print(my_cont.most_common()[0][0])#getting the specific key
print(my_cont.values())
print(my_cont.keys())
print(my_cont.items())

letters = Counter("mississippi")
print(letters)


# Update the counts of m and i
letters.update(m=3, i=4)
print(letters)


# Add a new key-count pair
letters.update({"a": 2})
print(letters)


# Update with another counter
letters.update(Counter(["s", "s", "p"]))
print(letters)


#msissing key does not raise a key error
letters = Counter("mississippi")
print(letters["a"])#default count will be zero



#multiset/multiplicity. multiset is the keys and the counter is the value, hence you can
#do math operations
inventory = Counter(dogs=23, cats=14, pythons=7)

adopted = Counter(dogs=2, cats=5, pythons=1)
inventory.subtract(adopted)
inventory


new_pets = {"dogs": 4, "cats": 1}
inventory.update(new_pets)
inventory


inventory = inventory - Counter(dogs=2, cats=3, pythons=1)
inventory


new_pets = {"dogs": 4, "pythons": 2}
inventory += new_pets
inventory
