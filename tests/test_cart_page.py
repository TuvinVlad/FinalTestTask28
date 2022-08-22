import pytest
from pages.dns_page import MainPage


#Проверяем функционал добавления товара в корзину
def test_check_add_basket(web_browser):

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()
    page.sort_btn.click()
    page.cheap_btn.click()  #Отсортировываем товар от min  до max
    page.wait_page_loaded()
    page.buy_btn.click()
    page.basket_btn.click()

    #Ожидаем, что мы оказываемся на странице корзины
    assert page.get_current_url() == 'https://www.dns-shop.ru/cart/'

    #Извлекаем число из счетчика товаров в корзине
    amount = page.counter_stuff.get_text()
    items = ' '.join(map(str, amount))
    res = [int(i) for i in items.split() if i.isdigit()]

    # Ожидаем, что количество товаров в корзине не равно нулю
    assert res != 0


#Проверяем функционал удаления добавленного в корзину товара
def test_check_refuse_stuff(web_browser):

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()
    page.sort_btn.click()
    page.cheap_btn.click()
    page.wait_page_loaded()
    page.buy_btn.click()
    page.basket_btn.click()
    page.ref_btn.click() #Нажимаем кнопку "Удалить"
    msg = page.basket_title.get_text() #Получаем текст сообщения на странице корзины

    #Ожидаем, что на странице корзины появится сообщение об удалении товаров
    assert 'Корзина пуста' in msg


#Проверяем кнопку перехода к оформлению заказа
def test_reg_order_btn(web_browser):

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()
    page.sort_btn.click()
    page.cheap_btn.click()
    page.wait_page_loaded()
    page.buy_btn.click()
    page.basket_btn.click()
    page.ord_reg_btn.click() #Жмем кнопку "Оформить"

    # Ожидаем, что мы оказываемся на странице оформления
    assert page.get_current_url() == 'https://www.dns-shop.ru/checkout/'