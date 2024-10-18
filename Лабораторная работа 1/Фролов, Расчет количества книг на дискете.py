# TODO Найдите количество книг, которое можно разместить на дискете
stranic = 100
strok = 50
simbol = 25
simvolume = 4
disceta_volume = 1.44 * 1024 * 1024

book_volume = stranic*strok*simbol*simvolume

amountofbooks = disceta_volume//book_volume

print("Количество книг, помещающихся на дискету:", int(amountofbooks))
