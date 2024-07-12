from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):#Данный класс стоновится потомком класса Base.

    url = 'https://www.citilink.ru/?_action=login&_success_login=1'##Создаём переменную url, чтобы мы могли обращаться к нужной странице.

    def __init__(self, driver):# Теперь мы обязаны передать сюда новую переменную super.Который говорит, что это именно потомок нашего класса.
        super().__init__(driver)
        self.driver = driver

    # Locators - переменные хранящие наши локаторы.

    cookie_button = '//span[text()="Я согласен"]'
    button_enter = '(//div[@data-meta-name="UserButtonContainer"])//div'
    email = '//input[@name="login"]'
    password = '//input[@name="pass"]'
    button_login = '(//span[text()="Войти"])[3]'


    # Getters - методы, которые указывают метод ожидания(Явное\Неявное) и указываем то, что элемент на странице должен, либо не должен быть кликабельным(.until).

    def get_cookie_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookie_button)))

    def get_button_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    # Actions - те действия, которые мы будем хранить в наших локаторах. Кликанье, сохранять информацию в поля и т.д.#

    def click_cookie_button(self):# Метод клика на принятие куки файлов.
        self.get_cookie_button().click()
        print("Click Coockie Button")

    def click_button_enter(self):# Метод нажатия на кнопку войти.
        self.get_button_enter().click()
        print("Click Button Enter")

    def input_email(self, email):# Метод ввода почтового адреса в поле.
        self.get_email().send_keys(email)
        print("Input User Name")

    def input_password(self, password):# Метод ввода пароля в поле.
        self.get_password().send_keys(password)
        print("Input Password")

    def click_button_login(self):# Метод нажатия на кнопку авторизации.
        self.get_button_login().click()
        print("Click Button Login")

    # Methods - создание основного метода, который будет передаваться в наш тест.

    def authorization(self):
        self.driver.get(self.url)#Метод, который будет открывать наш url.
        self.driver.maximize_window()# Вызываем метод открытия страницы во весь экран.
        self.get_current_url()# Вызываем метод отображения url страницы в консоли.
        self.click_cookie_button()# Вызываем метод нажатия на кнопку принятия cookie файлов.
        self.click_button_enter()# Вызываем метод нажатия на кнопку "Войти"
        self.input_email("i07433923@gmail.com")# Вызываем метод ввода email'a.
        self.input_password("TestPassword1234")# Вызываем метод ввода пароля.
        self.click_button_login()# Вызываем метод нажатия на кнопку авторизации.
        self.assert_url("https://www.citilink.ru/?_action=login&_success_login=1")# Вызываем метод сравнения url.