import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    
    def test_add_new_book_does_not_add_duplicate(self):

        collector = BooksCollector()

        collector.add_new_book('Тихий Дон')
        collector.add_new_book('Тихий Дон')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'book_name,expected',
        [
            ('Вторая жизнь Уве', True),
            ('ÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖ', True),
            ('Бабушка велела кланяться и передать, что просит прощения', False),
            ('', False),
        ]
    )

    def test_add_new_book_name_length(self, book_name, expected):

        collector = BooksCollector()

        collector.add_new_book(book_name)
        result = book_name in collector.get_books_genre()
        assert result == expected

    def test_get_books_with_specific_genre_returns_correct_books(self):

        collector = BooksCollector()

        collector.add_new_book('Нетопырь')
        collector.add_new_book('Ониксовый шторм')
        collector.set_book_genre('Нетопырь', 'Детективы')
        collector.set_book_genre('Ониксовый шторм', 'Фантастика')
        result = collector.get_books_with_specific_genre('Детективы')

        assert result == ['Нетопырь']


    def test_get_books_for_children_excludes_age_restricted_genres(self):

        collector = BooksCollector()

        collector.add_new_book('Нетопырь')
        collector.add_new_book('Винни Пух')
        collector.set_book_genre('Нетопырь', 'Детективы')
        collector.set_book_genre('Винни Пух', 'Мультфильмы')
        result = collector.get_books_for_children()

        assert 'Нетопырь' not in result
        assert 'Винни Пух' in result

    
    @pytest.mark.parametrize(

        'book_name, genre, is_for_children',
        [
            ('Ониксовый шторм', 'Фантастика', True),
            ('Том и Джерри', 'Мультфильмы', True),
            ('Оно', 'Ужасы', False),
            ('Нетопырь', 'Детективы', False)
        ]
    )

    def test_get_books_for_children_filters_by_genre(self, book_name, genre, is_for_children):

        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        result = collector.get_books_for_children()

        assert (book_name in result) == is_for_children

    def test_add_book_in_favorites_adds_only_existing_book(self):

        collector = BooksCollector()

        collector.add_new_book('Ониксовый шторм')
        collector.add_book_in_favorites('Ониксовый шторм')
        collector.add_book_in_favorites('Троя')

        assert collector.get_list_of_favorites_books() == ['Ониксовый шторм']

    def test_add_book_in_favorites_does_not_add_duplicate(self):

        collector = BooksCollector()

        collector.add_new_book('Ониксовый шторм')
        collector.add_book_in_favorites('Ониксовый шторм')
        collector.add_book_in_favorites('Ониксовый шторм')

        assert collector.get_list_of_favorites_books().count('Ониксовый шторм') == 1

    def test_delete_book_from_favorites_removes_book(self):

        collector = BooksCollector()

        collector.add_new_book('Ониксовый шторм')
        collector.add_book_in_favorites('Ониксовый шторм')
        collector.delete_book_from_favorites('Ониксовый шторм')

        assert 'Ониксовый шторм' not in collector.get_list_of_favorites_books()

    def test_get_book_genre_returns_empty_string_if_genre_not_set(self):

        collector = BooksCollector()

        collector.add_new_book('Мастер и Маргарита') 
        genre = collector.get_book_genre('Мастер и Маргарита')

        assert 'Мастер и Маргарита' in collector.get_books_genre()
        assert genre == ''

    def test_book_without_genre_not_in_specific_genre_list(self):

        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')

        result = collector.get_books_with_specific_genre('Фантастика')

        assert 'Мастер и Маргарита' not in result
        assert result == []