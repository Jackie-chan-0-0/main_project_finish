from base.base_class import Base


class Checkout_page(Base):#Создаём переменную url, чтобы мы могли обращаться к нужной страницу непосредственно из данного файла, а не из теста. И передаём параметры класса Base, через который мы обращаемся к нашему драйверу.
    #Данный класс стоновится потомком класса Base.

    def __init__(self, driver):# Теперь мы обязаны передать сюда новую переменную super.Который говорит, что это именно потомок нашего класса.
        super().__init__(driver)
        self.driver = driver

    # Locators - переменные хранящие наши локаторы.

    # Getters - методы, которые указывают метод ожидания(Явное\Неявное) и указываем то, что элемент на странице должен, либо не должен быть кликабельным(.until).

    # Actions - те действия, которые мы будем хранить в наших локаторах. Кликанье, сохранять информацию в поля и т.д.#

    # Methods

    def go_back(self):
        self.get_current_url()# Вызываем метод отображения url страницы в консоли.
        self.get_screenshot()
        self.driver.back()
        self.assert_url("https://www.citilink.ru/order/")