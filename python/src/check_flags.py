# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

# NB (alkurbatov): While this method is ok in general,
# better to use examples below.
if x == 1 or y == 1 or z == 1:  # noqa: FURB108
    print("passed")

if 1 in (x, y, z):
    print("passed")

# These only test for truthiness:
if x or y or z:  # noqa: FURB108
    print("passed")

if any((x, y, z)):
    print("passed")
