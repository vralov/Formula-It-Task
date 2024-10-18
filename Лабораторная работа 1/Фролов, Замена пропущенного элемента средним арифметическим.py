numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
for i in range(0, len(numbers)):
    if numbers[i] == None:
       j = i
       sum = 0
       numbers[j] = 0
       for l in range(0, len(numbers)):
           sum = sum + numbers[l]
       numbers[j] = sum/len(numbers)
print("Измененный список:", numbers)
