# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(str1,str2, a = ','):
    str1 = set(str1.split(a))
    str2 = set(str2.split(a))
    return sorted(list(str1 & str2))
print(find_common_participants(participants_first_group, participants_second_group, "|"))