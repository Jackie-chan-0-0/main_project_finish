import datetime
import time

from selenium.webdriver import ActionChains


class Base():#В данном классе хранятся параметры нашего драйвера.
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):# Создаём метод отображения url страницы, на которой мы находимся.
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):# Данный метод проверяет значение на странице.
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method screenshot"""

    def get_screenshot(self):# Данный метод делает скриншот.
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot.' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\DeephousePro\\PycharmProjects\\pythonProject\\main_project_finish\\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):# Общий метод сравнения url траницы с ожидаемым.
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method Move To Element""" # Общий метод перемещения к нужному локатору элемента на странице.

    def move_to_element(self, getter):
        actions = ActionChains(self.driver)
        actions.move_to_element(getter).perform()

    """Method Filter Click And Assert Value In Page""" # Общий метод сравнения значения количества товаров в фильтре до его нажатия со значением отображающимся на странице после его нажатия.

    def filter_click_and_assert_value_in_page(self, location_filter_click, location_value_in_page):
        value_1 = location_filter_click.text
        print(f"Value Checkbox_1 {value_1}")
        location_filter_click.click()
        print(f"Click Checkbox")
        time.sleep(2)
        value_2 = ''.join(filter(lambda x: x.isdigit(), list(location_value_in_page.text)))
        print(f"Value Page {value_2}")
        assert value_1 == value_2
        print(f"Good value number of products")

    """Метод добавления товара в корзину и сравнения цены и имени товара(до и после появления pop-up)""" # Общий метод сравнения значений имени и цены товара во всплывающем окне с теми же значениями выбранного товара на странице.

    def assert_price_and_name_phone(self, get_price_product_page, get_price_product_pop_up, get_name_product_page, get_name_product_pop_up):
        value_1 = f"[{get_price_product_page.text}, {get_name_product_page.text}]"
        print(value_1)
        value_2 = f"[{get_price_product_pop_up.text}, {get_name_product_pop_up.text}]"
        print(value_2)
        assert value_1 == value_2
        print("Good value price and name in pop-up")