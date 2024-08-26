first = input('Введите 1 число: ')
second = input('Введите 2 число: ')
third  = input('Введите 3 число: ')
int_first = int(float(first))
int_second = int(float(second))
int_tgird = int(float(third))
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
