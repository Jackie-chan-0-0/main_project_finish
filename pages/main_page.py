from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):# Теперь мы обязаны передать сюда новую переменную super.Который говорит, что это именно потомок нашего класса.
        super().__init__(driver)
        self.driver = driver

    # Locators
    city_button = '//button[@data-meta-name="CityChangeButton"]'
    search_city = '//input[@name="search-city"]'
    city = '((//div[@data-meta-name="CityList__searchResults"])//span)[2]'
    category_button = '//a[@data-meta-category="cardId-'

    # Getters
    def get_city_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_button)))

    def get_search_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_city)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_category_button(self, value):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'{self.category_button}{value}"]')))

    # Actions
    def click_city_button(self):
        self.get_city_button().click()
        print("Click City Button")

    def input_search_city(self, city):
        self.get_search_city().send_keys(city)
        print("Input City Good")

    def click_city(self):
        self.get_city().click()

    def click_phones_category_button(self):
        self.get_category_button(2).click()
        print("Click Phones Category Button")

    def click_monitors_category_button(self):
        self.get_category_button(4).click()
        print("Click Monitors Category Button")

    # Methods
    def choice_city(self):# Метод выбора города.
        self.click_city_button()# Вызываем метод нажатия на кнопку выбора города.
        self.input_search_city("Краснодар")# Вызываем метод ввода города в поле поиска.
        self.click_city()# Вызываем метод нажатия на найденный город.

    def category_phones(self):# Метод выбора категории Смартфоны.
        self.get_current_url()# Вызываем метод отображения url страницы в консоли.
        self.click_phones_category_button()# Вызываем метод нажатия на кнопку выбора Смартфонов.
        self.assert_url("https://www.citilink.ru/catalog/smartfony/")# Вызываем метод сравнения url.

    def category_monitors(self):# Метод выбора категории Мониторы.
        self.get_current_url()  # Вызываем метод отображения url страницы в консоли.
        self.click_monitors_category_button()  # Вызываем метод нажатия на кнопку выбора Мониторов.
        self.assert_url("https://www.citilink.ru/catalog/monitory/")
