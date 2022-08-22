import pytest
from pages.dns_page import MainPage


#Проверяем работу вертикального навигационного меню в левой части сайта
def test_nav_menu(web_browser):

    page = MainPage(web_browser)

    #Убираем всплывающее окно с вопросом о городе
    page.q_btn.click()
    page.wait_page_loaded()
    page.ap_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8e9b716404e77/bytovaya-texnika/'

    #Возвращаемся на главную страницу
    page.go_back()
    page.smart_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a890dc16404e77/smartfony-planshety-i-fototexnika/'

    page.go_back()
    page.tv_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8bfb516404e77/tv-i-multimedia/'

    page.go_back()
    page.comp_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17aa72ab16404e77/komplektuyushhie-kompyutery-i-noutbuki/'

    page.go_back()
    page.office_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8addb16404e77/ofis-i-set/'

    page.go_back()
    page.rest_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/7c3fa3257701c0c8/otdyx-i-razvlecheniya/'

    page.go_back()
    page.tool_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a9c2a316404e77/instrumenty/'

    page.go_back()
    page.const_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/dbb4f637c37f0606/stroitelstvo-i-remont/'

    page.go_back()
    page.hom_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/212b482fcdc66369/dom-dekor-i-kuxnya/'

    page.go_back()
    page.car_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a88ba616404e77/avtotovary/'

    page.go_back()
    page.acc_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/c644002fc427e92e/aksessuary-i-uslugi/'

    page.go_back()
    page.thrift_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/markdown/'


# Проверяем работу выпадающего меню "Покупателям" в шапке сайта
def test_customers_menu(web_browser):
    page = MainPage(web_browser)
    page.buyers_btn.click()
    page.ord_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/help/useful-information/8145d90b-1c3a-44c4-84b9-bb3f54aa783a/'

    page.buyers_btn.click()
    page.deliv_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/delivery/'

    page.buyers_btn.click()
    page.pay_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/help/useful-information/f112d810-a586-4c60-b651-8d328fe0e0e7/'

    page.buyers_btn.click()
    page.bonus_btn.click()  # Осуществляется переход на сторонний сайт 'https://prozapass.ru/'

    # Возвращаемся на сайт DNS
    page.get('https://www.dns-shop.ru/')
    page.buyers_btn.click()
    page.stat_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/order/check-order-status/'

    page.buyers_btn.click()
    page.exc_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/service-center/exchange-and-returns/'

    page.buyers_btn.click()
    page.loan_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/credit/'

    page.buyers_btn.click()
    page.serv_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/service-center/'

    page.buyers_btn.click()
    page.conf_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница соответствующего пункта меню откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/rules/policy/'


#Проверяем осуществление перехода на главную страницу при клике на лого в шапке сайта
def test_logo(web_browser):

    page = MainPage(web_browser)
    page.get('https://www.dns-shop.ru/catalog/17a8e9b716404e77/bytovaya-texnika/')
    page.logo_btn.click()

    assert page.get_current_url() == 'https://www.dns-shop.ru/'


#Проверяем работу кнопок блока "Акции"
def test_check_actions(web_browser):

    page = MainPage(web_browser)
    page.left_act_btn.click()
    page.wait_page_loaded()

    #Ожидаем, что при клике на кнопку осуществляется переход на соответствующую страницу
    assert page.get_current_url() == 'https://www.dns-shop.ru/actions/'

    page.go_back()
    page.right_act_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что при клике на кнопку осуществляется переход на соответствующую страницу
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/actions/'

    page.go_back()
    page.offer_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что при клике на кнопку осуществляется переход на соответствующую страницу
    assert page.get_current_url() == 'https://www.dns-shop.ru/actions/?types=1'

    page.go_back()
    page.ben_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что при клике на кнопку осуществляется переход на соответствующую страницу
    assert page.get_current_url() == 'https://www.dns-shop.ru/actions/?types=30'

    page.go_back()
    page.b_set_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что при клике на кнопку осуществляется переход на соответствующую страницу
    assert page.get_current_url() == 'https://www.dns-shop.ru/actions/?types=80'
