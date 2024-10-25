# TODO Найдите количество книг, которое можно разместить на дискете
import math
page = 100
line = 50
symbol = 25
symbol_volume = 4
diskette_volume = 1.44 * 1024 * 1024

book_volume = page * line * symbol * symbol_volume

amount_of_books = diskette_volume / book_volume

print("Количество книг, помещающихся на дискету:", math.floor(amount_of_books))

