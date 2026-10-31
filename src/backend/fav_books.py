class FavoriteBooks:

    def __init__(self):
        self.favorites = []

    """
    Add a book to the favorite books list,
    and the books list in the BookStore class if the book is not already in the list.
    """

    def add(self, book):
        if book not in self.favorites:
            self.favorites.append(book)

    def remove(self, book):
        if book in self.favorites:
            self.favorites.remove(book)
