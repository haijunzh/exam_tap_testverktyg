# User Story:
# As a user
# I want to add a book by entering its title and author
# So that I can expand the catalogue with new titles

# Acceptance Criteria:
# - The add-book form has "Titel" and "Författare" fields and a "Lägg till ny bok" button.
# - The submit button is disabled if either required field is blank.
# - Submitting a title and author adds the book to the catalogue.

Feature: Add a book to the catalogue

  Background:
    Given the user is on the start page
    When the user clicks on the "Lägg till bok" button

  Scenario Outline: User adds a book with a title and author
    When the user enters "<title>" in the "Titel" input field
    And the user enters "<author>" in the "Författare" input field
    And the user clicks on the "Lägg till ny bok" button
    And the user clicks on the "Katalog" button
    Then the user should see a book with the title "<title>" and author "<author>" in the catalogue

    Examples:
      | title                           | author          |
      | Mio, Mio                        | Astrid Lindgren |
      | The Wonderful Wizard of Oz      | L. Frank Baum   |

  Scenario Outline: User cannot add a book when a required field is blank
    When the user leaves the "<blank_field>" input field blank
    And the user enters "<value>" in the "<filled_field>" input field
    Then the "Lägg till ny bok" button should be disabled

    Examples:
      | blank_field | filled_field | value           |
      | Titel       | Författare   | Astrid Lindgren |
      | Författare  | Titel        | Mio, Mio        |

  Scenario: User cannot add a book when both fields are blank
    Then the "Lägg till ny bok" button should be disabled
