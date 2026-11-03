from behave import then, when
from playwright.sync_api import expect


@when('the user clicks on the "Mina böcker" button')
def step_user_clicks_favorite_books(context):
    context.page.get_by_role("button", name="Mina böcker").click()


@then("the user should see the empty favorites message")
def step_user_sees_empty_favorites_message(context):
    expect(
        context.page.get_by_text(
            "När du valt, kommer dina favoritböcker att visas här.", exact=True
        )
    ).to_be_visible()
    expect(context.page.get_by_role("listitem")).to_have_count(0)


@then(
    'the book should be appearing on the booklist of the page '
    'when the user clicks on the "Mina böcker" button'
)
def step_book_appears_in_favorites(context):
    context.page.get_by_role("button", name="Mina böcker").click()
    favorite = context.page.get_by_role("listitem").filter(
        has_text=context.book_title
    )
    expect(favorite).to_be_visible()


@then(
    'the book should not be appearing on the booklist of the page '
    'when the user clicks on the "Mina böcker" button'
)
def step_book_does_not_appear_in_favorites(context):
    context.page.get_by_role("button", name="Mina böcker").click()
    favorite = context.page.get_by_role("listitem").filter(
        has_text=context.book_title
    )
    expect(favorite).to_have_count(0)
