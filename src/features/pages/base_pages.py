class BasePage:
    def __init__(self, page):
        self.page = page
        self.add_players_button = page.get_by_role("button", name="Lägg till spelare")
        self.name_field = page.get_by_role("textbox")
        self.start_turn_button = page.get_by_role("button", name="Börja ditt drag")


    def navigate(self):
        self.page.goto("https://tap-vt26-testautomatisering.github.io/exam/", timeout=10_000)

    def add_player(self, name):
        self.name_field.fill(name)
        self.add_players_button.click()

#x = BasePage()