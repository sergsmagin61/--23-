Masgistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
DomKnigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
BukMarket = {'Пушкин', 'Достоевский', 'Маяковский'}
Galeria = {'Чехов', 'Тютчев', 'Пушкин'}
books = {'Грибоедов', 'Маяковский'}
shops = {'Masgistr', 'DomKnigi', 'BukMarket', 'Galeria'}

av_shops = [shop for shop in shops if len(books.difference(vars()[shop])) == 0]


print("Книги Грибоедова и Маяковского нельзя приобрести в магазинах:", av_shops)
