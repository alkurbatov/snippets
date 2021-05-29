# Init a list with X empty lists:
new_list = [[] for _ in range(5)]

print('[')
for i in new_list:
    print(f'\t{i}')
print(']')
