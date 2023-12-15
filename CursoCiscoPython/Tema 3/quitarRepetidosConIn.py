my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in my_list:
    if i in my_list:
        del my_list[i]

print("La lista con elementos únicos:")
print(my_list)
