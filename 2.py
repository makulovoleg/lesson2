l = input("Введите элементы списка: ").split()
l[:-1:2], l[1::2] = l[1::2], l[:-1:2]
print(l)