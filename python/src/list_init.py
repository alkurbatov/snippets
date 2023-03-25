from typing import List, Optional

# Init a list with X empty values:
new_list: List[Optional[int]] = [None] * 5
print(new_list)

# Init a list with X empty lists:
new_list_of_lists: List[List[int]] = [[] for _ in range(5)]
print(new_list_of_lists)
