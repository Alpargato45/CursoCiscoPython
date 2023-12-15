my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in my_list:
    aux = my_list[i]
    for j in range (1,len(my_list)):
        if(i == j):
            del my_list[j]

print("La lista con elementos únicos:")
print(my_list)
