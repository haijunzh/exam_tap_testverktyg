
# User Stories for LäsListan(Reading List)

### 1. View Book Catalogue
**As a** user  
**I want to** browse a catalogue of available books  
**So that** I can explore the collection and select my favorite books  

**Acceptance Criteria:**
- The catalogue displays a list of available books with their titles and authors.
- Each book in the catalogue provides an option to mark or select it as a favorite.

---

### 2. Add New Book
**As a** user  
**I want to** add a new book by entering its title and author  
**So that** I can expand the book catalogue with new titles  

**Acceptance Criteria:**
- Input fields for "Title" and "Author" are provided along with a submit button.
- Submitting valid details adds the book to the catalogue immediately.
- Proper validation ensures blank fields cannot be submitted.

---

### 3. View My Favorite Books
**As a** user  
**I want to** view a list dedicated to my favorite books  
**So that** I can easily keep track of the books I have favorited  

**Acceptance Criteria:**
- A dedicated section/page lists all books currently marked as favorites by the user.
- If no books are favorited, an appropriate empty state or message is displayed.

---

### 4. View Book Statistics
**As a** user  
**I want to** see statistics about the book collection  
**So that** I can get an overview of the total number of books and how many are marked as my favorites  

**Acceptance Criteria:**
- The statistics view displays the total count of books in the catalogue.
- The statistics view displays the count of books currently marked as favorites.
- Statistics update dynamically when books are favorited and de-favorited.
