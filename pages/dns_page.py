import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.dns-shop.ru/'

        super().__init__(web_driver, url)

    # Поле поиска
    search = WebElement(xpath='/html/body/header/nav/div/div[1]/form/div/input')

    # Кнопка поиска
    search_run_button = WebElement(xpath='/html/body/header/nav/div/div[1]/form/div/div[2]/span[2]')

    # Данные о товарах в результатах поиска
    products_titles = ManyWebElements(xpath='/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div[2]')


    #Кнопка, открывающая радио-селектор сортировки товаров:
    sort_btn = WebElement(xpath='/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]')
    #Кнопка сортировки по цене от min до max
    sort_products_by_price = WebElement(xpath='/html/body/div[8]/div/label[1]/span[1]')

    #Кнопки радио-селектора сортировки товаров:
    cheap_btn = WebElement(xpath='/html/body/div[8]/div/label[1]/span[1]')
    exp_btn = WebElement(xpath='html/body/div[8]/div/label[2]/span')
    pop_btn = WebElement(xpath='html/body/div[8]/div/label[3]/span')
    disc_btn = WebElement(xpath='html/body/div[8]/div/label[4]/span')
    nam_btn = WebElement(xpath='html/body/div[8]/div/label[5]/span')
    d_btn = WebElement(xpath='html/body/div[8]/div/label[6]/span')
    est_btn = WebElement(xpath='html/body/div[8]/div/label[7]/span')

    #Кнопка, открывающая радио-селектор группировки товаров:
    gr_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/span')

    #Кнопки радио-селектора группировки товаров:
    line_btn = WebElement(xpath='//div[9]/div/label[2]/span')
    dev_btn = WebElement(xpath='//div[9]/div/label[3]/span')
    have_btn = WebElement(xpath='//div[9]/div/label[4]/span')
    off_btn = WebElement(xpath='//div[9]/div/label[5]/span')
    mat_btn = WebElement(xpath='//div[9]/div/label[6]/span')
    cap_btn = WebElement(xpath='//div[9]/div/label[7]/span')
    vol_btn = WebElement(xpath='//div[9]/div/label[8]/span')
    col_btn = WebElement(xpath='//div[9]/div/label[9]/span')
    temp_btn = WebElement(xpath='//div[9]/div/label[10]/span')


    # Цены товаров в результатах поиска
    products_prices = ManyWebElements(xpath='/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div/div[4]/div/div[1]')

    # Проверка кнопок горизонтального меню сортировки товаров
    # Данные о товарах
    stuff_titles = ManyWebElements(xpath='//div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div/a/span')

    # Кнопка, разворачивающая меню
    expand_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[1]/i')

    # Кнопка, закрывающая ранее выбрранную страницу с отсортированным товаром
    res_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[2]/i')
    
    # Кнопки, открывающие страницы с товаром, отсортированным по определенному признаку
    m_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[2]')
    gl_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[3]')
    sm_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[4]')
    cer_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[5]')
    zav_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[6]')
    term_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[7]')
    light_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[7]')
    white_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[8]')
    zal_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[9]')
    a_off_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[10]')
    wire_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[11]')
    pict_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[12]')
    t_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[13]')
    move_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[14]')
    teaset_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[15]')

    # Кнопки для проверки функционала корзины
    buy_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/button[2]')
    basket_btn = WebElement(xpath='//div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/button[2]')
    counter_stuff = WebElement(xpath='//div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div/input')
    ref_btn = WebElement(xpath='//div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div/div[3]/div/div[2]/button[2]/p')
    basket_title = WebElement(xpath='//div/div[2]/div[2]/div[2]/div[1]')
    ord_reg_btn = WebElement(id='buy-btn-main')

    # Местоположение картинок
    stuff_images = ManyWebElements(xpath='//div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div/div[1]/a/picture/img')

    # Кнопка подтверждения города во всплывающем окне
    q_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[1]/div/div/div[2]/div[1]/div/button[1]')

    # Кнопки вертикального навигационного меню:
    ap_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[1]/div[1]/a')
    smart_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[2]/div[1]/a')
    tv_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[3]/div[1]/a')
    comp_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[4]/div[1]/a')
    office_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[5]/div[1]/a')
    rest_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[6]/div[1]/a')
    tool_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[7]/div[1]/a')
    const_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[8]/div[1]/a')
    hom_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[9]/div[1]/a')
    car_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[10]/div[1]/a')
    acc_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[11]/div[1]/a')
    thrift_btn = WebElement(xpath='//div[1]/div[1]/div[1]/div/div[12]/div[1]/a')

    # Кнопки меню "Покупателям"
    buyers_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[3]/a')
    ord_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[3]/ul/a[1]')
    deliv_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[3]/ul/a[2]')
    pay_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[3]/ul/a[3]')
    bonus_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[3]/ul/a[4]')
    stat_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[3]/ul/a[5]')
    exc_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[3]/ul/a[6]')
    loan_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[3]/ul/a[7]')
    serv_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[3]/ul/a[8]')
    conf_btn = WebElement(xpath='//header/div[3]/div/ul[1]/li[3]/ul/a[9]')

    # Кнопка лого в шапке сайта
    logo_btn = WebElement(id='header-logo')

    # Кнопки блока "Акции"
    left_act_btn = WebElement(xpath='//div[1]/div[1]/div[2]/div[3]/div/div[2]/a[1]')
    right_act_btn = WebElement(xpath='//div[1]/div[1]/div[2]/div[3]/div/div[2]/a[2]')
    offer_btn = WebElement(xpath='//div[1]/div[1]/div[2]/div[3]/div/div[1]/a[1]')
    ben_btn = WebElement(xpath='//div[1]/div[1]/div[2]/div[3]/div/div[1]/a[2]')
    b_set_btn = WebElement(xpath='//div[1]/div[1]/div[2]/div[3]/div/div[1]/a[3]')
