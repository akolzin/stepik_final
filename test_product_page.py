import pytest
import time
import random
from .pages.basket_page import BasketPage  # если не запускается добавить точку перед "pages.basket_page import BasketPage"  (разница пакетов)
from .pages.login_page import LoginPage  # если не запускается добавить точку перед "pages.login_page import LoginPage"  (разница пакетов)
from .pages.product_page import ProductPage  # если не запускается добавить точку перед "pages.product_page import ProductPage"  (разница пакетов)
from .pages.main_page import MainPage


# @pytest.mark.need_review
# def test_guest_can_add_product_to_basket(browser):
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     # stepik4.3.2
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     # stepik4.3.3
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_product_to_basket()
#     product_page.solve_quiz_and_get_code()
#     product_page.find_product_name()
#     product_page.find_product_price()


# @pytest.mark.need_review
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     product_page = MainPage(browser, link)
#     product_page.open()
#     product_page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# # @pytest.mark.parametrize('link', ["okay_link",pytest.param("bugged_link", marks=pytest.mark.xfail),"okay_link"])
# def test_guest_can_add_product_to_basket(browser, link):
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     # stepik4.3.4
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_product_to_basket()
#     # time.sleep(5)
#     product_page.solve_quiz_and_get_code()
#     product_page.find_product_name()
#     product_page.find_product_price()

# @pytest.mark.xfail(reason='wrong message')
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_product_to_basket()
#     product_page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_not_be_success_message()
#
# @pytest.mark.xfail(reason='dont dissapeared')
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_product_to_basket()
#     product_page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty_message()
    basket_page.is_basket_empty()
