# Examinationsprojekt för kursen Testautomatisering och testverktyg

## Backend
* Python-kod av läslistan i src-mapp:
1.	book_store.py → klassen BookStore ska ha följande metoder:
a.	addBook(author, title)
b.	toggleFavorite(book_id)
2.	fav_books.py → klassen FavoriteBooks ska ha följande metoder:
a.	add(book)
b.	remove(book)

* Test-kod 
1.	tests/unit/ → enhetstest för alla fyra metoder
2.	tests/integration/ → integrationstest för klasserna

## Teorifrågor
Svara kortfattat på följande frågor i ANSWERS.md för att demonstrera dina kunskaper.
1.	Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
2.	Beskriv hur det går till när man arbetar med TDD.
3.	Beskriv hur BDD skiljer sig från TDD.
4.	Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.
