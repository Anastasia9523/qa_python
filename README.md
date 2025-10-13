# Проект: QA Python

## Тесты

В рамках задания были реализованы тесты с использованием **pytest** для класса `BooksCollector`.

### Реализованные тесты

- **test_add_new_book_does_not_add_duplicate** — проверяет, что дубликат книги не добавляется
- **test_add_new_book_name_length** — проверяет ограничение длины названия (до 40 символов)  
- **test_get_books_with_specific_genre_returns_correct_books** — проверяет фильтрацию по жанру  
- **test_get_books_for_children_excludes_age_restricted_genres** — проверяет, что из детских исключаются книги с возрастным рейтингом 
- **test_add_book_in_favorites_adds_only_existing_book** - проверяет добавление книги в избранное (только если она есть в books_genre)
- **test_add_book_in_favorites_does_not_add_duplicate** - проверяет, что нельзя добавить одну и ту же книгу в избранное дважды
- **test_delete_book_from_favorites_removes_book** - проверяет удаление книги из избранного
- **test_get_book_genre_returns_empty_string_if_genre_not_set** - проверяет добавление книги без указания жанра
- **test_book_without_genre_not_in_specific_genre_list** - проверяет, что книга без жанра не появляется в списке по жанру
- **test_set_book_genre_sets_correct_genre** — проверяет корректное назначение жанра книге
- **test_get_book_genre_returns_correct_genre** — проверяет возвращение жанра для книги
- **test_get_books_genre_returns_full_dictionary** — проверяет получение полного словаря книг с жанрами
- **test_get_list_of_favorites_books_returns_correct_list** — проверяет корректный список избранных книг