numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
for i in range(0, len(numbers)):
    if numbers[i] is None:
        S = 0
        numbers[i] = 0
        for t in range(0, len(numbers)):
            S = S + numbers[t]
        numbers[i] = S / len(numbers)
print("Измененный список:", numbers)

