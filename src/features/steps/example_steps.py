from behave import given, then


@given("jag öppnar startsidan")
def step_open(context):
    context.page.goto("https://tap-vt26-testautomatisering.github.io/exam/")


@then('ska sidtiteln vara "{title}"')
def step_check_title(context, title):
    assert context.page.title() == title
