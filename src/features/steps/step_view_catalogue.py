import re

from behave import given, then, when
from playwright.sync_api import expect

from src.features.pages.base_pages import BasePage


def _book(context, title):
    return context.page.get_by_text(title, exact=False)


def _heart(context):
    return _book(context, context.book_title).get_by_role("button")


@given("the user is on the start page")
def step_user_is_on_start_page(context):
    context.base_page = BasePage(context.page)
    context.base_page.navigate()


@when('the user clicks on the "Katalog" button')
def step_user_clicks_catalogue(context):
    catalogue_button = context.page.get_by_role("button", name="Katalog")
    if catalogue_button.is_disabled():
        expect(context.page.get_by_text("Välj dina favoriter")).to_be_visible()
    else:
        catalogue_button.click()


@then('the user should see a promt text "Välj dina favoriter"')
def step_user_sees_favorites_prompt(context):
    expect(context.page.get_by_text("Välj dina favoriter")).to_be_visible()


@then('the user should see a book with the title "{title}" and author "{author}"')
def step_user_sees_book(context, title, author):
    book = _book(context, title)
    expect(book).to_be_visible()
    visible_text = "".join(book.inner_text().split()).casefold()
    expected_author = "".join(author.split()).casefold()
    assert expected_author in visible_text


@when(
    'the user is viewing a specific book "{title}" in the catalogue '
    "with the cursor hovering over the book's title and author"
)
def step_user_views_book_and_hovers(context, title):
    book = _book(context, title)
    expect(book).to_be_visible()
    book.hover()
    context.book_title = title


@when(
    "the user clicks the appearing heart icon beside the book "
    "to mark it as a favorite"
)
def step_user_marks_book_as_favorite(context):
    _heart(context).click()


@then("the heart icon should change to filled")
def step_heart_icon_is_filled(context):
    expect(_heart(context)).to_have_class(re.compile(r"\bselected\b"))


@when(
    "the user clicks the filled heart icon beside the book "
    "to remove it from favorites"
)
def step_user_removes_book_from_favorites(context):
    heart = _heart(context)
    expect(heart).to_have_class(re.compile(r"\bselected\b"))
    heart.click()


@then("the heart icon should change to empty")
def step_heart_icon_is_empty(context):
    expect(_heart(context)).not_to_have_class(re.compile(r"\bselected\b"))


@then(
    'the book should be appearing on the booklist of the page '
    'when the user clicks on the "Mina böcker" button'
)
def step_book_appears_in_favorites(context):
    context.page.get_by_role("button", name="Mina böcker").click()
    book = context.page.get_by_role("listitem").filter(
        has_text=context.book_title
    )
    expect(book).to_be_visible()


@then(
    'the book should not be appearing on the booklist of the page '
    'when the user clicks on the "Mina böcker" button'
)
def step_book_does_not_appear_in_favorites(context):
    context.page.get_by_role("button", name="Mina böcker").click()
    book = context.page.get_by_role("listitem").filter(
        has_text=context.book_title
    )
    expect(book).to_have_count(0)
