import pytest
from pages.auth_page1 import AuthPage

def test_authorisation(web_browser):

    page = AuthPage(web_browser)

    page.first_btn.click()

    page.pre_btn.click()

    page.pas_btn.click()

    page.phone.send_keys('8 952 586 43 44')

    page.password.send_keys("prada378")

    page.enter_btn.click()

    page.ready_btn.click()
    page.prof_btn.click()

    assert page.get_current_url() == 'https://profile.dns-shop.ru/'



def test_exit_profile(web_browser):

    page = AuthPage(web_browser)

    page.first_btn.click()

    page.pre_btn.click()

    page.pas_btn.click()
    page.field_btn.click()

    page.phone.send_keys('8 952 586 43 44')

    page.password.send_keys("prada378")

    page.enter_btn.click()

    page.ready_btn.click()
    page.prof_btn.click()
    page.exit_btn.click()

    assert page.get_current_url() == 'https://profile.dns-shop.ru/uniformProfile/personal/unauthorized/'