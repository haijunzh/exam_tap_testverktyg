import pytest

from src.backend.book_store import BookStore
from src.backend.fav_books import FavoriteBooks


@pytest.mark.unit
def test_add_book():
    # Strategy: Test the add_book method of the BookStore class
    # Create a BookStore instance
    # Create fake/mock
    # Call the method add_book()
    # Assert that the book is added to the books list
    # Assert that the book is not in the fav_books list

    store = BookStore()

    author = "F. Scott Fitzgerald"
    title = "The Great Gatsby"
    book_id = store.add_book(author, title)

    assert book_id in store.books
    assert store.books[book_id]["author"] == author
    assert store.books[book_id]["title"] == title
    assert store.books[book_id]["favorite"] is False


@pytest.mark.unit
def test_toggle_favorite(mocker):
    mock_favorite_books = mocker.Mock(spec=FavoriteBooks)
    store = BookStore(mock_favorite_books)

    author = "F. Scott Fitzgerald"
    title = "The Great Gatsby"
    book_id = store.add_book(author, title)

    # 1. Första toggle -> Boken markeras som favorit
    store.toggle_favorite(book_id)
    assert store.books[book_id]["favorite"] is True
    mock_favorite_books.add.assert_called_once_with(store.books[book_id])
    mock_favorite_books.remove.assert_not_called()

    # 2. Andra toggle -> Boken tas bort från favoriter
    store.toggle_favorite(book_id)
    assert store.books[book_id]["favorite"] is False
    mock_favorite_books.remove.assert_called_once_with(store.books[book_id])
