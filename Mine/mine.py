from RPA.Browser.Selenium import Selenium
import time

URL = "https://blaze-4.com/pt/games/mines?modal=auth"
email = "informe seu email"
senha = "Informe sua senha"

BET_START_VALUE = "0,01"
BOMB_AMOUNT = "2"
CLICK_LIST = [0, 2, 4, 5, 7, 9, 10, 12, 14]

class SeleniumScraper:

    def __init__(self,url, bet_start_value, bomb_amount, click_list):
        self.browser_lib = Selenium()
        self.url = url
        self.bet_start_value = bet_start_value
        self.bomb_amount = bomb_amount
        self.click_list = click_list

    def open_website(self):
        self.browser_lib.open_available_browser(self.url)
        self.browser_lib.maximize_browser_window()

    def main(self):
        self.open_website()
        self.make_login()
        self.set_value_entry()
        self.play_game()
        input()

    def is_bomb(self, path):
        try:
            self.browser_lib.element_text_should_be(path, "class" "cell-stop is-bomb")
        except:
            return False
        return True

    def play_game(self):
        start_button_path = "//button[normalize-space()='Começar o jogo']"
        self.browser_lib.click_element(start_button_path)
        time.sleep(3)
        for value in range(0, 25):
            if value in self.click_list:
                path = f"//div[@id='{value}']"
                self.browser_lib.click_element(path)
                time.sleep(1)
                if self.is_bomb(path):
                    print("Perdeu, clicamos em uma bomba!")
                retira_button_path = "//button[contains(text(), 'Retirar')]"
                self.browser_lib.click_element(retira_button_path)
                print('O procsso termi')

    def set_value_entry(self):
        time.sleep(5)
        label_path = "//input[@data-testid='amount']"
        self.browser_lib.click_element(label_path)
        self.browser_lib.input_text(label_path, self.bet_start_value)
        label_bomb_path = "//select[@name='select']"
        self.browser_lib.select_from_list_by_value(label_bomb_path, self.bomb_amount)

    def close_website(self):
        self.browser_lib.close_browser()

    def make_login(self):
        login_btn_path = "//button[normalize-space()='Entrar']"
        self.browser_lib.wait_until_page_contains_element(locator=login_btn_path)
        input_email_path = "//input[@name='username']"
        senha_input_path = "//input[@name='password']"
        self.browser_lib.input_text(input_email_path, email)
        self.browser_lib.input_text(senha_input_path, senha)
        self.browser_lib.click_element(login_btn_path)

if __name__ == '__main__':
    obj = SeleniumScraper(
        url=URL,bet_start_value=BET_START_VALUE,
        bomb_amount=BOMB_AMOUNT,
        click_list=CLICK_LIST )
    obj.main()

