# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(participants_first_group, participants_second_group, separator=","):
    group1 = participants_first_group.split(separator)
    group2 = participants_second_group.split(separator)

    identical_participants = list(set(group1) & set(group2))

    identical_participants.sort()

    return identical_participants

# TODO Провеьте работу функции с разделителем отличным от запятой
