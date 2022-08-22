from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.dns-shop.ru/?city=taganrog'
        super().__init__(web_driver, url)


    #Окно ввода номера телефона
    phone = WebElement(xpath='/html/body/header/nav/div/div[1]/div[3]/div/div[1]/div[2]/modal/div/div/div/div[2]/div/input')

    #Окно ввода пароля
    password = WebElement(xpath='/html/body/header/nav/div/div[1]/div[3]/div/div[1]/div[2]/modal/div/div/div/div[3]/div/input')

    #Кнопка "Войти" в шапке сайта
    first_btn = WebElement(xpath='//*[@id="user-menu"]/div[1]/div[2]/div[1]')
    pre_btn = WebElement(xpath='//*[@id="user-menu"]/div/div[3]/div[2]/div/div[1]/button')
    pas_btn = WebElement(xpath='//*[@id="user-menu"]/div[1]/div[2]/modal/div/div/div/div[4]/div[2]/div/div/div[2]')
    #field_btn = WebElement(xpath='//*[@id="user-menu"]/div[1]/div[2]/modal/div/div/div/div[2]/div')
    #field2_btn = WebElement(xpath='/html/body/header/nav/div/div[1]/div[3]/div/div[1]/div[2]/modal/div/div/div/div[3]/div')
    enter_btn = WebElement(xpath='//*[@id="user-menu"]/div[1]/div[2]/modal/div/div/div/div[6]/div')
    ready_btn = WebElement(class_name='user-profile__level')
    prof_btn = WebElement(xpath='//*[@id="user-menu"]/div/div[3]/div[2]/div/ul/li[9]/a')
    exit_btn = WebElement(xpath='//header/div/a[2]')
