import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        """Фикстура, возвращающая новый экземпляр BooksCollector перед каждым тестом."""
        return BooksCollector()

    def test_add_new_book_does_not_add_duplicate(self):

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

        collector.add_new_book(book_name)
        result = book_name in collector.get_books_genre()
        assert result == expected

    def test_get_books_with_specific_genre_returns_correct_books(self):

        collector.add_new_book('Нетопырь')
        collector.add_new_book('Ониксовый шторм')
        collector.set_book_genre('Нетопырь', 'Детективы')
        collector.set_book_genre('Ониксовый шторм', 'Фантастика')
        result = collector.get_books_with_specific_genre('Детективы')

        assert result == ['Нетопырь']


    def test_get_books_for_children_excludes_age_restricted_genres(self):

        collector.add_new_book('Нетопырь')
        collector.add_new_book('Винни Пух')
        collector.set_book_genre('Нетопырь', 'Детективы')
        collector.set_book_genre('Винни Пух', 'Мультфильмы')
        result = collector.get_books_for_children()

        assert 'Нетопырь' not in result
        assert 'Винни Пух' in result

    def test_add_book_in_favorites_adds_only_existing_book(self):

        collector.add_new_book('Ониксовый шторм')
        collector.add_book_in_favorites('Ониксовый шторм')
        collector.add_book_in_favorites('Троя')

        assert collector.get_list_of_favorites_books() == ['Ониксовый шторм']

    def test_add_book_in_favorites_does_not_add_duplicate(self):

        collector.add_new_book('Ониксовый шторм')
        collector.add_book_in_favorites('Ониксовый шторм')
        collector.add_book_in_favorites('Ониксовый шторм')

        assert collector.get_list_of_favorites_books().count('Ониксовый шторм') == 1

    def test_delete_book_from_favorites_removes_book(self):

        collector.add_new_book('Ониксовый шторм')
        collector.add_book_in_favorites('Ониксовый шторм')
        collector.delete_book_from_favorites('Ониксовый шторм')

        assert 'Ониксовый шторм' not in collector.get_list_of_favorites_books()

    def test_get_book_genre_returns_empty_string_if_genre_not_set(self):

        collector.add_new_book('Мастер и Маргарита') 
        genre = collector.get_book_genre('Мастер и Маргарита')

        assert 'Мастер и Маргарита' in collector.get_books_genre()
        assert genre == ''

    def test_book_without_genre_not_in_specific_genre_list(self):

        collector.add_new_book('Мастер и Маргарита')

        result = collector.get_books_with_specific_genre('Фантастика')

        assert 'Мастер и Маргарита' not in result
        assert result == []

    def test_set_book_genre_sets_correct_genre(self, collector):
        collector.books_genre = {'Тихий Дон': ''}
        collector.set_book_genre('Тихий Дон', 'Классика')

        assert collector.books_genre['Тихий Дон'] == 'Классика'

    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.books_genre = {'Тихий Дон': 'Классика'}
        genre = collector.get_book_genre('Тихий Дон')

        assert genre == 'Классика'

    def test_get_books_genre_returns_full_dictionary(self, collector):
        collector.books_genre = {
            'Тихий Дон': 'Классика',
            'Винни Пух': 'Мультфильмы'
        }

        result = collector.get_books_genre()

        assert result == {
            'Тихий Дон': 'Классика',
            'Винни Пух': 'Мультфильмы'
        }

    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.favorites = ['Тихий Дон', 'Винни Пух']

        result = collector.get_list_of_favorites_books()

        assert result == ['Тихий Дон', 'Винни Пух']