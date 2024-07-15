from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    filter_price_min = '(//input[@name="input-min"])[3]'
    filter_price_max = '(//input[@name="input-max"])[3]'
    checkbox_filter_label = '//div[@data-meta-name="FilterLabel"]'
    number_products_page = '//span[@data-meta-name="SubcategoryPageTitle__product-count"]'
    filter_drop_down = '//div[@data-meta-name="FilterDropdown"]'
    price_product = '//div[@data-meta-name="SnippetProductVerticalLayout"]'
    name_phone = '//a[@data-meta-name="Snippet__title"]'
    price_in_pop_up = '((//div[@data-meta-name="UpsaleBasketProductDetails"])//span[@data-meta-is-total="notTotal"])//span'
    name_phone_in_pop_up = '((//div[@data-meta-name="UpsaleBasketProductDetails"])//div)[4]'
    closed_pop_up_button = '//button[@data-meta-name="UpsaleBasket__close-popup"]'
    go_to_shopping_cart_button = '//span[text()="Перейти в корзину"]'
    basket_snippet = '//div[@data-meta-name="BasketSnippet"]'

    # Getters

    def get_filter_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_min)))

    def get_filter_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_max)))

    def get_checkbox_filter_sup(self, value):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"({self.checkbox_filter_label})[{value}]//sup")))

    def get_number_of_products_in_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_products_page)))

    def get_filter_drop_down(self, value):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"({self.filter_drop_down})[{value}]//span")))

    def get_price_product(self, value):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'(({self.price_product})[{value}]//span[@data-meta-is-total="notTotal"])//span')))

    def get_name_phone(self, value):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"({self.name_phone})[{value}]")))

    def get_price_in_pop_up(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_in_pop_up)))

    def get_name_phone_in_pop_up(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_phone_in_pop_up)))

    def get_closed_pop_up_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.closed_pop_up_button)))

    def get_go_to_shopping_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_shopping_cart_button)))

    def get_price_next_window(self, value):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'((({self.basket_snippet})[{value}])//span[@data-meta-is-total="notTotal"])//span')))

    def get_name_next_window(self, value):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"((({self.basket_snippet})[{value}])//span)[3]")))

    # Actions

    def input_filter_price_min(self, price):# метод ввода фильтра минимальной цены.
        self.move_to_element(self.get_filter_price_min())
        self.get_filter_price_min().clear()
        self.get_filter_price_min().send_keys(price)
        print(f"Input Filter Price Minimum {price} GOOD")

    def input_filter_price_max(self, price):# метод ввода фильтра максимальной цены.
        self.driver.execute_script("window.scrollTo(0, 650);")
        self.get_filter_price_max().clear()
        self.get_filter_price_max().send_keys(price)
        print(f"Input Filter Price Maximum {price} GOOD")

    def click_checkbox_filter_available(self):# метод нажатия на чекбокс фильтра "Доступен самовывоз".
        self.filter_click_and_assert_value_in_page(self.get_checkbox_filter_sup(1), self.get_number_of_products_in_page())# вызываем метод сравнения значения количества товаров на фильтре и на сайте.
        print("Click Checkbox Filter Available GOOD")

    def click_checkbox_available_in_installments(self):# метод нажатия на чекбокс фильтра "Доступно в рассрочку".
        self.filter_click_and_assert_value_in_page(self.get_checkbox_filter_sup(3), self.get_number_of_products_in_page())# вызываем метод сравнения значения количества товаров на фильтре и на сайте.
        print("Click Checkbox Available In Installments GOOD")

    def click_checkbox_20_discount_phone(self):# метод нажатия на чекбокс фильтра "20% и больше" на смартфоны.
        self.filter_click_and_assert_value_in_page(self.get_checkbox_filter_sup(10), self.get_number_of_products_in_page())# вызываем метод сравнения значения количества товаров на фильтре и на сайте.
        print("Click Checkbox 20% Discount GOOD")

    def click_checkbox_20_discount_monitor(self):# метод нажатия на чекбокс фильтра "20% и больше" на мониторы.
        self.filter_click_and_assert_value_in_page(self.get_checkbox_filter_sup(10), self.get_number_of_products_in_page())# вызываем метод сравнения значения количества товаров на фильтре и на сайте.
        print("Click Checkbox 20% Discount GOOD")

    def click_checkbox_load_rating_phone_sup(self):# метод нажатия на чекбокс фильтра "4,5 и выше".
        self.filter_click_and_assert_value_in_page(self.get_checkbox_filter_sup(13), self.get_number_of_products_in_page())# вызываем метод сравнения значения количества товаров на фильтре и на сайте.

    def click_checkbox_load_rating_monitor_sup(self):# метод нажатия на чекбокс фильтра "4,5 и выше".
        self.filter_click_and_assert_value_in_page(self.get_checkbox_filter_sup(12), self.get_number_of_products_in_page())# вызываем метод сравнения значения количества товаров на фильтре и на сайте.

    def click_year_of_release_filter_drop_down(self):# метод нажатия кнопку drop down "Год выпуска".
        self.move_to_element(self.get_filter_drop_down(23))
        self.get_filter_drop_down(23).click()
        print("Click Opening Button Year Of Release GOOD")

    def click_response_time_filter_drop_down(self):# метод нажатия кнопку drop down "Время отклика".
        self.move_to_element(self.get_filter_drop_down(22))
        self.get_filter_drop_down(22).click()
        print("Click Opening Button Response Time GOOD")

    def click_checkbox_2024(self):# метод нажатия на чекбокс фильтра "2024".
        self.move_to_element(self.get_checkbox_filter_sup(97))
        self.filter_click_and_assert_value_in_page(self.get_checkbox_filter_sup(97), self.get_number_of_products_in_page())# вызываем метод сравнения значения количества товаров на фильтре и на сайте.
        print("Click Checkbox 2024 GOOD")

    def click_checkbox_5ms(self):# метод нажатия на чекбокс фильтра "3 мс."
        self.move_to_element(self.get_checkbox_filter_sup(86))
        self.filter_click_and_assert_value_in_page(self.get_checkbox_filter_sup(86), self.get_number_of_products_in_page())# вызываем метод сравнения значения количества товаров на фильтре и на сайте.
        print("Click Checkbox 5ms Good")

    def click_price_product_1_and_accert_values(self):# метод нажатия на кнопку добавления в корзину первого товара.
        self.move_to_element(self.get_price_product(1))
        self.get_price_product(1).click()
        print("Click Add to cart Product 1")
        self.assert_price_and_name_phone(self.get_price_product(1), self.get_price_in_pop_up(), self.get_name_phone(1), self.get_name_phone_in_pop_up())# вызываем метод сравнения параметров "Имя" и "Цена" во всплывающем окне.

    def click_closed_pop_up_button(self):# метод нажатия на крестик закрытия всплывающего окна.
        self.get_closed_pop_up_button().click()
        print("Click Closed Pop_up Button")

    def click_price_product_2_and_accert_values(self):# метод нажатия на кнопку добавления в корзину второго товара
        self.get_price_product(3).click()
        print("Click Add to cart Product 2")
        self.assert_price_and_name_phone(self.get_price_product(3), self.get_price_in_pop_up(), self.get_name_phone(3), self.get_name_phone_in_pop_up())# вызываем метод сравнения параметров "Имя" и "Цена" во всплывающем окне.

    def click_phone_go_to_shopping_cart_button(self):# метод нажатия на кнопку перехода в корзину и сравнения параметов товаров с параметрами в корзине.
        values_page_1 = f"[{self.get_price_product(1).text}, {self.get_price_product(3).text}, {self.get_name_phone(1).text}, {self.get_name_phone(3).text}]"
        print(values_page_1)
        self.get_go_to_shopping_cart_button().click()
        print("Click Go To Shopping Cart Button")
        value_price_page_2 = f"[{self.get_price_next_window(2).text}, {self.get_price_next_window(1).text}, {self.get_name_next_window(2).text}, {self.get_name_next_window(1).text}]"
        print(value_price_page_2)
        assert values_page_1 == value_price_page_2
        print("Good value price and name")

    def click_monitor_go_to_shopping_cart_button(self):
        values_page_1 = f"[{self.get_price_product(1).text}, {self.get_price_product(3).text}, {self.get_name_phone(1).text}, {self.get_name_phone(3).text}]"
        print(values_page_1)
        self.get_go_to_shopping_cart_button().click()
        print("Click Go To Shopping Cart Button")
        value_price_page_2 = f"[{self.get_price_next_window(1).text}, {self.get_price_next_window(2).text}, {self.get_name_next_window(1).text}, {self.get_name_next_window(2).text}]"
        print(value_price_page_2)
        assert values_page_1 == value_price_page_2
        print("Good value price and name")

    # Methods

    def filtering_phones(self):
        self.get_current_url()# Вызываем метод отображения url страницы в консоли.
        self.input_filter_price_min(10000)# Вызываем метод ввода фильтра минимальной цены.
        self.input_filter_price_max(100000)# Вызываем метод ввода фильтра максимальной цены.
        self.click_checkbox_filter_available()# Вызываем метод нажатия на чекбокс фильтра "Доступен самовывоз". И сравнение значения количества товаров на фильтре и на сайте.
        self.click_checkbox_available_in_installments()# Вызываем метод нажатия на чекбокс фильтра "Доступно в рассрочку". И сравнение значения количества товаров на фильтре и на сайте.
        self.click_checkbox_20_discount_phone()# Вызываем метод нажатия на чекбокс фильтра "20% и больше". И сравнение значения количества товаров на фильтре и на сайте.
        self.click_checkbox_load_rating_phone_sup()# Вызываем метод нажатия на чекбокс фильтра "4,5 и выше". И сравнение значения количества товаров на фильтре и на сайте.
        self.click_year_of_release_filter_drop_down()# Вызываем метод нажатия кнопку drop down "Год выпуска".
        self.click_checkbox_2024()# Вызываем метод нажатия на чекбокс фильтра "2024". И сравнение значения количества товаров на фильтре и на сайте.
        self.click_price_product_1_and_accert_values()# Вызываем метод нажатия на кнопку добавления в корзину первого товара и сравнение параметров "Имя" и "Цена" во всплывающем окне.
        self.click_closed_pop_up_button()#Вызываем метод нажатия на крестик закрытия всплывающего окна.
        self.click_price_product_2_and_accert_values()# Вызываем метод нажатия на кнопку добавления в корзину второго товара и сравнение параметров "Имя" и "Цена" во всплывающем окне.
        self.click_phone_go_to_shopping_cart_button()# Вызываем метод нажатия на кнопку перехода в корзину и сравнения параметов товаров с параметрами в корзине.
        self.assert_url("https://www.citilink.ru/order/")# Вызываем метод сравнения url.

    def filtering_monitors(self):
        self.get_current_url()  # Вызываем метод отображения url страницы в консоли.
        self.input_filter_price_min(10000)  # Вызываем метод ввода фильтра минимальной цены.
        self.input_filter_price_max(100000)  # Вызываем метод ввода фильтра максимальной цены.
        self.click_checkbox_filter_available()  # Вызываем метод нажатия на чекбокс фильтра "Доступен самовывоз". И сравнение значения количества товаров на фильтре и на сайте.
        self.click_checkbox_available_in_installments()  # Вызываем метод нажатия на чекбокс фильтра "Доступно в рассрочку". И сравнение значения количества товаров на фильтре и на сайте.
        self.click_checkbox_20_discount_monitor()  # Вызываем метод нажатия на чекбокс фильтра "20% и больше". И сравнение значения количества товаров на фильтре и на сайте.
        self.click_checkbox_load_rating_monitor_sup()  # Вызываем метод нажатия на чекбокс фильтра "4,5 и выше". И сравнение значения количества товаров на фильтре и на сайте.
        self.click_response_time_filter_drop_down()# Вызываем метод нажатия кнопку drop down "Время отклика".
        self.click_checkbox_5ms()# Вызываем метод нажатия на чекбокс фильтра "3 мс."
        self.click_price_product_1_and_accert_values()  # Вызываем метод нажатия на кнопку добавления в корзину первого товара и сравнение параметров "Имя" и "Цена" во всплывающем окне.
        self.click_closed_pop_up_button()  # Вызываем метод нажатия на крестик закрытия всплывающего окна.
        self.click_price_product_2_and_accert_values()  # Вызываем метод нажатия на кнопку добавления в корзину второго товара и сравнение параметров "Имя" и "Цена" во всплывающем окне.
        self.click_monitor_go_to_shopping_cart_button()  # Вызываем метод нажатия на кнопку перехода в корзину и сравнения параметов товаров с параметрами в корзине.
        self.assert_url("https://www.citilink.ru/order/")# Вызываем метод сравнения url.
