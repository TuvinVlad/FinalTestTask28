import pytest
from pages.dns_page import MainPage


#Проверяем работу поиска на сайте
def test_check_main_search(web_browser):

    page = MainPage(web_browser)

    page.search.send_keys('чайник')
    page.search_run_button.click()

    # Убеждаемся, что пользователь видит список товаров:
    assert page.products_titles.count() >= 1

    # Убеждаемся, что пользователь видит соответствующие его запросу товары:
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'чайник' in title.lower(), msg


#Убеждаемся, что ввод с неправильной раскладкой клавиатуры срабатывает
def test_check_wrong_input_in_search(web_browser):

    page = MainPage(web_browser)

    # Пытаемся ввести "чайник" с английской раскладкой:
    page.search.send_keys('xfqybr')
    page.search_run_button.click()

    # Убеждаемся, что пользователь видит список товаров:
    assert page.products_titles.count() >= 1

    # Убеждаемся, что пользователь видит соответствующие его запросу товары:
    for title in page.products_titles.get_text():
        msg = 'В поиске неверно введено название товара "{}"'.format(title)
        assert 'чайник' in title.lower(), msg