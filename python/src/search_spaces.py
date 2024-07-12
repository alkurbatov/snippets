"""Different ways of determing whether a string contains spaces."""

import re
import timeit

TEXT = "this is a long long long long long string"
SPACE_REGEX = re.compile(r"\s")

linear_search_using_in = """
' ' in TEXT
"""

linear_search_using_isspace = """
for char in TEXT:
    if char.isspace():
        break
"""

linear_search_using_regexp = """
re.search(r'\\s', TEXT)
"""

linear_search_using_compiled_regexp = """
re.search(SPACE_REGEX, TEXT)
"""

timing = timeit.timeit(linear_search_using_in, globals=globals(), number=100000)
print(f"Linear search using in: {timing}")

timing = timeit.timeit(linear_search_using_isspace, globals=globals(), number=100000)
print(f"Linear search using isspace: {timing}")

timing = timeit.timeit(linear_search_using_regexp, globals=globals(), number=100000)
print(f"Linear search using regexp: {timing}")

timing = timeit.timeit(
    linear_search_using_compiled_regexp, globals=globals(), number=100000
)
print(f"Linear search using compiled regexp: {timing}")
