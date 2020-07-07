import pytest
import time
import random
# from .pages.basket_page import BasketPage  # если не запускается добавить точку перед "pages.basket_page import BasketPage"  (разница пакетов)
from .pages.login_page import LoginPage  # если не запускается добавить точку перед "pages.login_page import LoginPage"  (разница пакетов)
from .pages.product_page import ProductPage  # если не запускается добавить точку перед "pages.product_page import ProductPage"  (разница пакетов)
from .pages.main_page import MainPage

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    time.sleep(5)
    product_page.find_product_name()
    product_page.find_product_price()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = MainPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()















