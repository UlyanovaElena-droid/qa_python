from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1 Тест для add_new_book больше 40 символов
    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        long_name = 'a' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre


    # 2 Тест для set_book_genre  
    # есть название и жанр
    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Термоядерный синтез Древнего Рима')
        collector.set_book_genre('Термоядерный синтез Древнего Рима', 'Ужасы')
        assert collector.books_genre['Термоядерный синтез Древнего Рима'] == 'Ужасы'

    # 3 Тест для get_book_genre
    def test_get_book_genre_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Термоядерный синтез Древнего Рима')
        collector.set_book_genre('Термоядерный синтез Древнего Рима', 'Ужасы')
        assert collector.get_book_genre('Термоядерный синтез Древнего Рима') == 'Ужасы'

    # 4 Тест для get_books_with_specific_genre (параметризованный)
    @pytest.mark.parametrize('genre,expected', [
        ('Ужасы', ['Термоядерный синтез Древнего Рима']),
        ('Комедии', []),
        ('Приключения', []),
    ])
    def test_get_books_with_specific_genre(self, genre, expected):
        collector = BooksCollector()
        collector.add_new_book('Термоядерный синтез Древнего Рима')
        collector.set_book_genre('Термоядерный синтез Древнего Рима', 'Ужасы')

        assert collector.get_books_with_specific_genre(genre) == expected

    # 5 Тест для get_books_genre
    def test_get_books_genre_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Термоядерный синтез Древнего Рима')
        collector.set_book_genre('Термоядерный синтез Древнего Рима', 'Ужасы')

        expected = {'Термоядерный синтез Древнего Рима': 'Ужасы'}

        assert collector.get_books_genre() == expected 

    # 6 Тест для get_books_for_children
    def test_get_books_for_children_restricted_age(self):
        collector = BooksCollector()
        collector.add_new_book('Термоядерный синтез Древнего Рима')
        collector.set_book_genre('Термоядерный синтез Древнего Рима', 'Ужасы')

        assert collector.get_books_for_children() == []

    # 7 Тест для add_book_in_favorites
    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Термоядерный синтез Древнего Рима')
        collector.add_book_in_favorites('Термоядерный синтез Древнего Рима')
        collector.add_book_in_favorites('Термоядерный синтез Древнего Рима')
        
        assert len(collector.favorites) == 1 

    # 8 Тест для delete_book_from_favorites
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Термоядерный синтез Древнего Рима')
        collector.add_book_in_favorites('Термоядерный синтез Древнего Рима')
        
        collector.delete_book_from_favorites('Термоядерный синтез Древнего Рима')
        
        assert 'Термоядерный синтез Древнего Рима' not in collector.favorites
        assert len(collector.favorites) == 0

    # 9 Тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []



