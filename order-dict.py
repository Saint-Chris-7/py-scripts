from collections import OrderedDict

from collections import OrderedDict

letters = OrderedDict(b=2, d=4, a=1, c=3)
letters


# Move b to the right end
letters.move_to_end("b")
print(letters)


# Move b to the left end
letters.move_to_end("b", last=False)
print(letters)


# Sort letters by key
for key in sorted(letters):
    letters.move_to_end(key)


print(letters)



# Regular dictionaries compare the content only
letters_0 = dict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, d=4, c=3)
print(letters_0 == letters_1)


# Ordered dictionaries compare content and order
letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = OrderedDict(b=2, a=1, d=4, c=3)
print(letters_0 == letters_1)


letters_2 = OrderedDict(a=1, b=2, c=3, d=4)
print(letters_0 == letters_2)

