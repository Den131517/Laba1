# TODO Найдите количество книг, которое можно разместить на дискете
Vol_disk = 1.44     # Мегабайт
Vol_disk_KiloB = Vol_disk * 1024    # Килобайт
Vol_disk_B = Vol_disk_KiloB * 1024      # Байт

Pages = 100     # Страниц
Lines_Pages = Pages * 50       # Строчек на 50 страниц
Symbols = Lines_Pages * 25     # Символов на 50 страницах

need = Symbols * 4      # надо байтов для всех символов
Books = Vol_disk_B / need

print("Количество книг, помещающихся на дискету:", round(Books,))
