import time

from selenium.webdriver.common.by import By


class TestDifferentLanguage:
    button_ru_text = "Добавить в корзину"
    button_en_text = "Add to basket"

    def test_different_language(self, driver):
        dr = driver.get('browser')
        dr.get("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        # time.sleep(30)
        add_button = dr.find_element(By.XPATH, "//button[contains(@class, 'add-to-basket')]")
        if driver.get('language') == 'ru':
            assert TestDifferentLanguage.button_ru_text, add_button.text
        else:
            assert TestDifferentLanguage.button_en_text, add_button.text
