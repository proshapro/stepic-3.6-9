import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    # Следующую строчку раскомментировать для визуальной проверки языка интерфейса (критерий 2):
    # time.sleep(30)
    assert WebDriverWait(browser, 12).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".add-to-basket button"))), "Button 'Add to basket' is not displayed on this page!"
