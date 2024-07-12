import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    basket_snippet = '//div[@data-meta-name="BasketSnippet"]'
    v_total_price = '((//div[@data-meta-name="Price"])//span)[3]'
    purchase = '//button[@title="Перейти к оформлению"]'
    v_total_price_page_2 = '((//div[@data-meta-name="Aside__wrapper"])//span)[16]'
    button_delete_action = '//div[@data-meta-name="DeleteAction"]'
    button_account = '(//div[@class="fresnel-container fresnel-greaterThanOrEqual-tabletL "])[4]//div'
    button_logout = '//a[@data-meta-name="ProfileMenu_Item_Выйти"]'

    # Getters

    def get_v_price_product(self, value):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'((({self.basket_snippet})[{value}])//span[@data-meta-is-total="notTotal"])//span')))

    def get_v_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.v_total_price)))

    def get_purchase(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.purchase)))

    def get_v_total_price_page_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.v_total_price_page_2)))

    def get_button_delete_action(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_delete_action)))

    def get_button_account(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_account)))

    def get_button_logout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_logout)))

    # Actions

    def assert_total_price(self):
        s_1 = self.get_v_price_product(1).text.replace(' ', '')
        s_2 = self.get_v_price_product(2).text.replace(' ', '')
        summ = int(s_1) + int(s_2)
        summ_finish = str(summ)
        assert summ_finish == self.get_v_total_price().text.replace(' ', '')
        print("Total Price GOOD")

    def click_purchase(self):
        v_total_price_1 = self.get_v_total_price().text
        self.get_purchase().click()
        print("Click Purchase")
        assert v_total_price_1 == self.get_v_total_price_page_2().text
        print("Good value total price")

    def click_button_delete_action(self):
        self.get_button_delete_action().click()
        time.sleep(2)
        print("Product delete GOOD")

    def click_button_account(self):
        self.get_button_account().click()
        print("Click Button Account Good")

    def click_button_logout(self):
        self.get_button_logout().click()
        print("Click Button Logout Good")

    # Methods

    def making_purchase(self):
        self.get_current_url()# Вызываем метод отображения url страницы в консоли.
        self.assert_total_price()# Вызываем метод сравнения сложенных сумм товаров с общей суммой.
        self.click_purchase()# Вызываем метод нажатия на кнопку "Перейти к оформлению"
        self.assert_url("https://www.citilink.ru/order/checkout/")# Вызываем метод сравнения url.

    def clear_cart(self):
        self.get_current_url()# Вызываем метод отображения url страницы в консоли.
        self.click_button_delete_action()# Вызываем метод удаления товара из корзины.
        self.click_button_delete_action()# Вызываем метод удаления товара из корзины.

    def logout_account(self):
        self.click_button_account()# Вызываем метод нажатия на кнопку авторизации.
        self.click_button_logout()# Вызываем метод нажатия на кнопку выхода.