def read_base():
    with open("D:\XXXXXXXXXXXXXXX\phone_book.txt", 'r') as f:
        str_val = f.read()
    str_val = str_val.split('), (')
    str_val = [x.replace("'", "").replace('[(', '').replace(')]', '') for x in str_val]
    return str_val

def print_phone(temp_list_1):
    try:
        max_len_fam_in_list = max([len(x.split(',')[0]) for x in temp_list_1])
        max_len_name_in_list = max([len(x.split(',')[1]) for x in temp_list_1])
        len_num = len(temp_list_1)
        for i, o in enumerate(temp_list_1):
            n_str_list = o.split(',')
            print(f'{str(i).rjust(len_num, " ")}) {n_str_list[0].ljust(max_len_fam_in_list, " ")} {n_str_list[1].ljust(max_len_name_in_list, " ")}: {n_str_list[2]}')
        print('')
    except:
        print('Данных, отвечающих условиям поиска, не найдено.')
        print('')

def find_user(ph_book, sel_name):
    temp_list = [x for x in ph_book if sel_name in x]
    return temp_list

def find_number(ph_book, sel_num):
    temp_list = [x for x in ph_book if sel_num in x]
    return temp_list

def add_user_phone(ph_book, fam, name, phone):
    text_str = f'{fam}, {name}, {phone}'
    ph_book.append(text_str)
    return ph_book
    
def delete_user(ph_book, sel):
    ind = ph_book.index(sel)
    print(f'Информация о пользователе {sel} будет удалена')
    select_go = int(input('1 - Удалить, 0 - отменить удаление '))
    if select_go == 1:
        ph_book.pop(ind)
        print('Информация удалена.')
        return ph_book
    else:
        pass
    
def exit_from_programm(ph_book):
    new_phone_book = []
    for i in ph_book:
        word_3 = i.split(', ')
        new_phone_book.append((word_3[0], word_3[1], word_3[2]))
                
    with open("D:\D:\XXXXXXXXXXXXXXX\phone_book.txt", 'w') as f:
        f.write(str(new_phone_book))


user_names = []
phone_book = read_base()
n = True

while n:
    print('   Выберите пункт меню:   ')
    print('')
    print('1. Поиск пользователя по имени или фамилии.')
    print('2. Поиск пользователя по номеру телефона.')
    print('3. Добавить пользователя.')
    print('4. Удалить пользователя.')
    print('')
    print('0. Завершение работы с программой.')
    select_val = input('Введите нужную цифру и нажмите Enter: ')
    print('')
    
    if select_val == '1':
        print('Введите имя или фамилию. Допускается несколько символов, идущих подряд.')
        select_name = input('По окончании ввода нажмите Enter ')
        print()
        temp_list = find_user(phone_book, select_name)
        print_phone(temp_list)
        
    elif select_val == '2':
        print('Введите номер телефона полностью или фрагмент.')
        print('Формат ввода номера: +7-901-174-23-15.')
        select_num = input('По окончании ввода нажмите Enter ')
        print('')
        temp_list = find_number(phone_book, select_num)
        print_phone(temp_list)
        
    elif select_val == '3':
        fam_val = input('Укажите фамилию пользователя. ')
        name_val = input('Имя пользователя. ')
        num_val = input('Введите номер телефона в формате: +7-901-174-23-15. ')
        add_user_phone(phone_book, fam_val, name_val, num_val)
        print('Информация добавлена в телефонную книгу и будет записана по окончании работы программы.')
        print('')
        
    elif select_val == '4':
        print('Укажите фрагмент фамилии или номера телефона пользователя. ')
        str_val = input('По окончании ввода нажмите Enter ')
        temp_txt = find_user(phone_book, str_val)
        print_phone(temp_txt)
        print('Введите номер напротив строки пользователя, которого нужно удалить.')
        sel = int(input('По окончании ввода нажмите Enter. '))
        str_val = temp_txt[sel]
        phone_book = delete_user(phone_book, str_val)
        print('')
    
    else:
        exit_from_programm(phone_book)
        print('Информация обновлена и записана.')
        print('Работа программы завершена.')
        n = False