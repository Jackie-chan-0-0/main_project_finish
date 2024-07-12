import time
import pytest

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.checkout_page import Checkout_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.order_page import Order_page
from pages.product_page import Product_page

def test_buy_product_1():# Создаём метод.

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.choice_city()
    mp.category_phones()

    fp = Product_page(driver)
    fp.filtering_phones()

    op = Order_page(driver)
    op.making_purchase()

    cp = Checkout_page(driver)
    cp.go_back()

    op.clear_cart()
    op.logout_account()

    print("Finish Test 1")
    time.sleep(10)
    driver.quit()

def test_buy_product_2():

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start Test 2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.choice_city()
    mp.category_monitors()

    pp = Product_page(driver)
    pp.filtering_monitors()

    op = Order_page(driver)
    op.making_purchase()

    cp = Checkout_page(driver)
    cp.go_back()

    op.clear_cart()
    op.logout_account()

    print("Finish Test 2")
    time.sleep(10)
    driver.quit()