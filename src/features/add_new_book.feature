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

  Scenario: User adds a book with a title and author
    When the user enters "Mio, Mio" in the "Titel" input field
    And the user enters "Astrid Lindgren" in the "Författare" input field
    And the user clicks on the "Lägg till ny bok" button
    And the user clicks on the "Katalog" button
    Then the user should see a book with the title "Mio, Mio" and author "Astrid Lindgren" in the catalogue

  Scenario: User cannot add a book without a title
    When the user leaves the "Titel" input field blank
    And the user enters "Astrid Lindgren" in the "Författare" input field
    Then the "Lägg till ny bok" button should be disabled

  Scenario: User cannot add a book without an author
    When the user enters "Mio, Mio" in the "Titel" input field
    And the user leaves the "Författare" input field blank
    Then the "Lägg till ny bok" button should be disabled

  Scenario: User cannot add a book when both fields are blank
    Then the "Lägg till ny bok" button should be disabled
