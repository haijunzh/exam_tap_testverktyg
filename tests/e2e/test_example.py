from playwright.sync_api import Page, expect


def test_title(page: Page):
    page.goto("/exam/")
    expect(page).to_have_title("Läslistan")
