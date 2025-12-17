# -*- coding: utf-8 -*-
# Информационная система "Библиотека" (Вариант 4)

class Book:
    """Класс, представляющий книгу."""
    def __init__(self, title, author, year, isbn, in_stock=True):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.in_stock = in_stock # True - книга в библиотеке, False - выдана

    def __str__(self):
        status = "В наличии" if self.in_stock else "Выдана"
        return f'"{self.title}", {self.author} ({self.year}), ISBN: {self.isbn} - {status}'

class Library:
    """Класс, представляющий библиотеку."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Добавляет новую книгу в каталог."""
        self.books.append(book)
        print(f'Книга "{book.title}" добавлена в каталог.')

    def find_book_by_title(self, title):
        """Ищет книгу по названию."""
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def give_book(self, isbn):
        """Выдает книгу читателю (меняет статус)."""
        for book in self.books:
            if book.isbn == isbn and book.in_stock:
                book.in_stock = False
                print(f'Книга "{book.title}" выдана.')
                return
        print("Книга не найдена или уже выдана.")

    def return_book(self, isbn):
        """Возвращает книгу в библиотеку."""
        for book in self.books:
            if book.isbn == isbn and not book.in_stock:
                book.in_stock = True
                print(f'Книга "{book.title}" возвращена.')
                return
        print("Книга не найдена или не была выдана.")

    def show_all_books(self):
        """Показывает весь каталог."""
        if not self.books:
            print("Каталог пуст.")
        for book in self.books:
            print(book)

# ===== Пример работы системы =====
def main():
    # Создаем библиотеку
    my_lib = Library()

    # Создаем несколько книг
    book1 = Book("Мастер и Маргарита", "М.А. Булгаков", 1966, "123-456")
    book2 = Book("Преступление и наказание", "Ф.М. Достоевский", 1866, "789-012")
    book3 = Book("1984", "Джордж Оруэлл", 1949, "345-678")

    # Добавляем книги в каталог (используем локальный репозиторий для фиксации на Шаге 4)
    my_lib.add_book(book1)
    my_lib.add_book(book2)
    my_lib.add_book(book3)

    print("\n--- Весь каталог ---")
    my_lib.show_all_books()

    # Имитация выдачи и возврата книги
    print("\n--- Выдача книги с ISBN 123-456 ---")
    my_lib.give_book("123-456")

    print("\n--- Поиск книги по слову 'преступление' ---")
    found = my_lib.find_book_by_title("преступление")
    for b in found:
        print(b)

    print("\n--- Каталог после выдачи ---")
    my_lib.show_all_books()

    print("\n--- Возврат книги с ISBN 123-456 ---")
    my_lib.return_book("123-456")

    print("\n--- Финальный каталог ---")
    my_lib.show_all_books()

if __name__ == "__main__":
    main()