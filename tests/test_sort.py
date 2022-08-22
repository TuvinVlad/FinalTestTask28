import pytest
from pages.dns_page import MainPage


#Проверяем функцию сортировки товаров по цене
def test_check_sort_by_price(web_browser):

    page = MainPage(web_browser)

    page.search.send_keys('чайник')
    page.search_run_button.click()

    # Делаем прокрутку до элемента до клика по нему, чтобы убедиться, что он виден в реальном браузере:
    page.sort_products_by_price.scroll_to_element()
    page.sort_btn.click()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    #Получаем цены на товары в результатах поиска:
    my_prices = page.products_prices.get_text()
    prices = ' '.join(map(str, my_prices))

    all_prices = [int(i) for i in prices.split() if i.isdigit()]

    # Убеждаемся в корректной работе сортировки:
    assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"


#Проверяем работу радио-селектора сортировки товаров
def test_check_radio(web_browser):

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()
    page.sort_btn.click()

    #Проверяем кнопку сортировки по цене от min до max
    page.cheap_btn.click()
    page.wait_page_loaded()

    #Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.sort_btn.click()
    #Проверяем кнопку сортировки по цене от max до min
    page.exp_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=2&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.sort_btn.click()
    # Проверяем кнопку сортировки по популярности
    page.pop_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=6&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.sort_btn.click()
    # Проверяем кнопку сортировки по скидке
    page.disc_btn.click()
    page.wait_page_loaded()
    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=7&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.sort_btn.click()
    # Проверяем кнопку сортировки по наименованию
    page.nam_btn.click()
    page.wait_page_loaded()
    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=3&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.sort_btn.click()
    # Проверяем кнопку сортировки по обсуждаемости
    page.d_btn.click()
    page.wait_page_loaded()
    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=4&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.sort_btn.click()
    # Проверяем кнопку сортировки по лучшей оценке
    page.est_btn.click()
    page.wait_page_loaded()
    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=5&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'


#Проверяем работу радио-селектора группировки товаров
def test_check_radio_group(web_browser):

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()
    page.gr_btn.click()
    page.line_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=6&groupBy=series&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.gr_btn.click()
    page.dev_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=6&groupBy=brand&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.gr_btn.click()
    page.have_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=6&groupBy=avails&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.gr_btn.click()
    page.off_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=6&groupBy=6541&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.gr_btn.click()
    page.mat_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=6&groupBy=2oj&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.gr_btn.click()
    page.cap_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=6&groupBy=2oi&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.gr_btn.click()
    page.vol_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=6&groupBy=2nz&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.gr_btn.click()
    page.col_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=6&groupBy=5j5&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'

    page.gr_btn.click()
    page.temp_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/17a8c8d116404e77/elektrochajniki/?order=6&groupBy=2os&q=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA&stock=now-today-tomorrow-later-out_of_stock'



#Проверяем работу кнопок горизонтального меню сортировки товаров
def test_check_classif_btns(web_browser):

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()
    page.m_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/cf09fab9e05c73b9/metalliceskie/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    #Закрываем ранее выбрранную страницу с отсортированным товаром
    page.res_btn.click()
    page.gl_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/f12fda0722bc3030/steklannye/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.sm_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/5d441401829aede8/umnye/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.cer_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/9b5146aa8fe6c89f/keramiceskie/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.zav_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/6a6c73eef8b14f09/s-zavarnikom/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.term_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/885f26a0ae5a892f/s-termoregulatorom/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()

    #Разворачиваем меню
    page.expand_btn.click()
    page.light_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/0c4b9221ff4fbb33/s-podsvetkoj/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.expand_btn.click()
    page.white_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/d2fa74b77ab1270b/belye/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.expand_btn.click()
    page.zal_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/22944af7fdf1d470/zaliv-vody-bez-otkrytia-kryski/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.expand_btn.click()
    page.a_off_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/59e27bdf5ebaacff/s-avtomaticeskim-otkluceniem/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.expand_btn.click()
    page.wire_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/1e2535273bb3196d/s-otsekom-dla-hranenia-snura/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.expand_btn.click()
    page.pict_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/940aa391247d5e42/s-risunkom-na-korpuse/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.expand_btn.click()
    page.t_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/c8a178da8266c6c2/s-effektom-termosa/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.expand_btn.click()
    page.move_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/214a337825b0e0c4/semnye-kryski/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1

    page.res_btn.click()
    page.expand_btn.click()
    page.teaset_btn.click()
    page.wait_page_loaded()

    # Ожидаем, что страница с отсортированными товарами откроется нормально
    assert page.get_current_url() == 'https://www.dns-shop.ru/catalog/recipe/66daf1806667bf00/cajnye-nabory/'
    # Убеждаемся, что пользователь видит список товаров:
    assert page.stuff_titles.count() >= 1