import pytest
from pages.dns_page import MainPage


#Проверяем наличие картинок у товаров
def test_check_images(web_browser):

    page = MainPage(web_browser)

    page.search.send_keys('пылесос')
    page.search_run_button.click()
    images = page.stuff_images

    # Узнаем количество картинок, отнимая от общего числа ячеек в соответствующем столбце не содержащие изображений
    for item in images:
        count = 0
        if item.get_attribute('src') == '':
            count -= 1
            # Ожидаем, что картинки есть у всех товаров в результатах поиска
            assert count == len(images)



