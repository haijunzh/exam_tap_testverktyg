from behave import then, when
from playwright.sync_api import expect


@when('the user clicks on the "Lägg till bok" button')
def step_user_opens_add_book_form(context):
    context.page.get_by_role("button", name="Lägg till bok").click()


@when('the user enters "{value}" in the "{field}" input field')
def step_user_enters_book_details(context, value, field):
    context.page.get_by_role("textbox", name=field).fill(value)


@when('the user leaves the "{field}" input field blank')
def step_user_leaves_book_field_blank(context, field):
    context.page.get_by_role("textbox", name=field).fill("")


@when('the user clicks on the "Lägg till ny bok" button')
def step_user_submits_new_book(context):
    context.page.get_by_role("button", name="Lägg till ny bok").click()


@then(
    'the user should see a book with the title "{title}" and author "{author}" '
    "in the catalogue"
)
def step_user_sees_added_book(context, title, author):
    book = context.page.get_by_text(title, exact=False)
    expect(book).to_be_visible()
    expect(book).to_contain_text(author)


@then('the "Lägg till ny bok" button should be disabled')
def step_add_book_button_is_disabled(context):
    expect(
        context.page.get_by_role("button", name="Lägg till ny bok")
    ).to_be_disabled()