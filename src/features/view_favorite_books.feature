# User Story: View My Favorite Books
# **As a** user  
# **I want to** view a list dedicated to my favorite books  
# **So that** I can easily keep track of the books I have favorited  

# **Acceptance Criteria:**
# - A dedicated section/page lists all books currently marked as favorites by the user.
# - If no books are favorited, an appropriate empty state or message is displayed.

Feature: View favorite books

  Scenario Outline: User views a book in their favorites
    Given the user is on the start page
    When the user clicks on the "Katalog" button
    And the user is viewing a specific book "<title>" in the catalogue with the cursor hovering over the book's title and author
    And the user clicks the appearing heart icon beside the book to mark it as a favorite
    Then the book should be appearing on the booklist of the page when the user clicks on the "Mina böcker" button

    Examples:
      | title                       |
      | The Pragmatic Procrastinator |
      | The Bugs are Coming          |

  Scenario: User views favorites when none have been selected
    Given the user is on the start page
    When the user clicks on the "Mina böcker" button
    Then the user should see the empty favorites message
