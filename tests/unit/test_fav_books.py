import pytest

from src.backend.fav_books import FavoriteBooks

@pytest.mark.unit
def test_initial_favorites_is_empty():
    favorites = FavoriteBooks()
    assert favorites.favorites == []
    
    
@pytest.mark.unit
def test_add_book_to_favorites():
    favorites = FavoriteBooks()
    book = {"id": 1, "author": "F. Scott Fitzgerald", "title": "The Great Gatsby", "favorite": True}
    
    favorites.add(book)
    
    assert book in favorites.favorites
    assert len(favorites.favorites) == 1
    
    book = {"id": 2, "author": "Astrid Lingren", "title": "Mio, Mio", "favorite": True}
    favorites.add(book)
    
    assert book in favorites.favorites
    assert len(favorites.favorites) == 2
    
@pytest.mark.unit
def test_remove_book_from_favorites():
    favorites = FavoriteBooks()
    book1 = {"id": 1, "author": "F. Scott Fitzgerald", "title": "The Great Gatsby", "favorite": True}
    book2 = {"id": 2, "author": "Astrid Lingren", "title": "Mio, Mio", "favorite": True}
    
    favorites.add(book1)
    favorites.add(book2)
    
    assert len(favorites.favorites) == 2
    
    favorites.remove(book1)
    
    assert book1 not in favorites.favorites
    assert len(favorites.favorites) == 1
    
    favorites.remove(book2)
    
    assert book2 not in favorites.favorites
    assert len(favorites.favorites) == 0

