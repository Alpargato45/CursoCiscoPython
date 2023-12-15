print("Di tu numero")
c0 = int(input())
pasos = 0

while c0 <= 0:
    print("Di tu numero")
    c0 = int(input())
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0//2
        pasos = pasos+1
        print(c0)
    else:
        c0 = 3 * c0 + 1
        pasos = pasos+1
        print(c0)
print("pasos = ", pasos)