x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

# Python merges dictionary keys
# in the order listed in the expression, overwriting
# duplicates from left to right.
#
# Works in Python 3.5+
print({**x, **y})
