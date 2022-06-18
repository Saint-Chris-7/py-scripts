from collections import ChainMap

dad = {"name": "John", "age": 35}
mom = {"name": "Jane", "age": 31}
family = ChainMap(mom, dad)
family


son = {"name": "Mike", "age": 0}
family = family.new_child(son)

for person in family.maps:
    print(person)

print(family.parents)

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

alpha_nums = ChainMap(numbers, letters)
alpha_nums


# Add a new key-value pair
alpha_nums["c"] = "C"
alpha_nums


# Pop a key that exists in the first dictionary
alpha_nums.pop("two")

print(alpha_nums)

# Delete keys that don't exist in the first dict but do in others
del alpha_nums["a"]


# Clear the dictionary
alpha_nums.clear()
print(alpha_nums)
