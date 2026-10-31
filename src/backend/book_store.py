from src.backend.fav_books import FavoriteBooks


class BookStore:
    def __init__(self, favorite_books=None):
        self.books = {}
        self.next_id = 1
        # Om ingen skickas med används den riktiga klassen som standard
        self.favorite_books = (
            favorite_books if favorite_books is not None else FavoriteBooks()
        )

    def add_book(self, author, title):
        book_id = self.next_id
        book = {"id": book_id, "author": author, "title": title, "favorite": False}
        self.books[book_id] = book
        self.next_id += 1
        return book_id

    def toggle_favorite(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            book["favorite"] = not book["favorite"]

            if book["favorite"]:
                self.favorite_books.add(book)
            else:
                self.favorite_books.remove(book)
