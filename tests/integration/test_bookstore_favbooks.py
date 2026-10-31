import pytest

from src.backend.book_store import BookStore
from src.backend.fav_books import FavoriteBooks

@pytest.mark.integration
def test_bookstore_favorite_books__integration():

    # Create instances of BookStore and FavoriteBooks
    favorite_books = FavoriteBooks()
    store = BookStore(favorite_books)

    # Add a book to the bookstore
    author = "F. Scott Fitzgerald"
    title = "The Great Gatsby"
    book_id = store.add_book(author, title)

    # Toggle the book as favorite
    store.toggle_favorite(book_id)

    # Assert that the book is marked as favorite in the bookstore
    assert store.books[book_id]["favorite"] is True

    # Assert that the book is added to the favorites list
    assert store.books[book_id] in favorite_books.favorites

    # Toggle the book again to remove it from favorites
    store.toggle_favorite(book_id)

    # Assert that the book is no longer marked as favorite in the bookstore
    assert store.books[book_id]["favorite"] is False

    # Assert that the book is removed from the favorites list
    assert store.books[book_id] not in favorite_books.favorites
