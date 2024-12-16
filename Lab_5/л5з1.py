class Book():
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def get_info(self):
        print(f'Название книги: {self.title}; Автор: {self.author}; Год издания: {self.year}')
book1=Book("Богатый папа, бедный папа","Роберт Кийосаки и Шэрон Л Лектер", 1997)
book1.get_info()