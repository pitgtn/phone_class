# Написать программу, которая принимает номера телефонов в формате:
# +XX-XXX-XXX-XX-XX
# и
# +XX-XXXXXXXXXX
# код страны может быть как однозначным, так и двузначным
# программа так же должна понимать формат, когда вместо +XX подается 8
# Введенные номера должны храниться в памяти, а при вводе пользователем буквы W (большое или маленькое) - записываться в файл phones.txt, каждый номер телефона на отдельной строчке. При повторном запуске программы, если файл уже есть, программа должна считать телефоны оттуда. Дубликаты в файле должны исключаться.
# При вводе all должны выводиться все номера, пронумерованные в порядке их появления в файле.
# При вводе просто числа должны выводиться телефоны под соответствующим индексом.
#  При выводе номер должен выводиться только в формате +XX-XXX-XXX-XX-XX
from phonenumber import PhoneNumber

print("Список команд:\n Q(q) - выход\n W(w) - запись в файл\n F(f) - вывод допустимых форматов номеров телефонов\n "
      "X(x)* - * =  порядковому номеру в списке")
input("+-+-+-+-\nНажмите enter для продолжения\n+-+-+-+-")
while True:
    input_user= input("Введите номер или Q для выхода: ").lower() or "f" # Если значение не введено, тогда a='f'
    if input_user== 'q':
        break
    else:
        PhoneNumber.check_enter(input_user)


