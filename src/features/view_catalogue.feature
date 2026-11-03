
# User Story: View Book Catalogue
# **As a** user  
# **I want to** browse a catalogue of available books  
# **So that** I can explore the collection and select my favorite books  

# **Acceptance Criteria:**
# - The catalogue displays a list of available books with their titles and authors.
# - Each book in the catalogue provides an option to mark or select it as a favorite.

Feature: View Book Catalogue

  Scenario Outline: User views a book in the catalogue
    Given the user is on the start page
    When the user clicks on the "Katalog" button
    Then the user should see a promt text "Välj dina favoriter"
    And the user should see a book with the title "<title>" and author "<author>"

    Examples:
      | title                       | author             |
      | The Pragmatic Procrastinator | Dave Thomasson     |
      | The Bugs are Coming          | George R.R.Martin  |

  Scenario Outline: User marks a book as favorite
    Given the user is on the start page
    When the user clicks on the "Katalog" button
    And the user is viewing a specific book "<title>" in the catalogue with the cursor hovering over the book's title and author
    When the user clicks the appearing heart icon beside the book to mark it as a favorite
    Then the heart icon should change to filled
    And the book should be appearing on the booklist of the page when the user clicks on the "Mina böcker" button

    Examples:
      | title                       |
      | The Pragmatic Procrastinator |
      | The Bugs are Coming          |

  Scenario Outline: User deselects a book as favorite
    Given the user is on the start page
    When the user clicks on the "Katalog" button
    And the user is viewing a specific book "<title>" in the catalogue with the cursor hovering over the book's title and author
    When the user clicks the appearing heart icon beside the book to mark it as a favorite
    When the user clicks the filled heart icon beside the book to remove it from favorites
    Then the heart icon should change to empty
    And the book should not be appearing on the booklist of the page when the user clicks on the "Mina böcker" button

    Examples:
      | title                       |
      | The Pragmatic Procrastinator |
      | The Bugs are Coming          |
