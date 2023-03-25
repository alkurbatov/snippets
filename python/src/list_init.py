# Init a list with X empty values:
new_list: list[int | None] = [None] * 5
print(new_list)

# Init a list with X empty lists:
new_list_of_lists: list[list[int]] = [[] for _ in range(5)]
print(new_list_of_lists)
