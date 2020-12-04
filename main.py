from classes import PhoneNumber

print("Список команд:\n Q(q) - выход\n W(w) - запись в файл\n F(f) - вывод допустимых форматов номеров телефонов\n "
      "X(x)* - * =  порядковому номеру в списке")
input("+-+-+-+-\nНажмите enter для продолжения\n+-+-+-+-")
while True:
    input_user= input("Введите номер или Q для выхода: ").lower() or "f" # Если значение не введено, тогда a='f'
    if input_user== 'q':
        break
    else:
        PhoneNumber.check_enter(input_user)


