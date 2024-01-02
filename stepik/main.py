import math
import os.path
import traceback

from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def start_test(url, func):
    with webdriver.Chrome() as driver:
        driver.get(url)
        func(driver)
        alert = driver.switch_to.alert
        print(alert.text)


def test_one(driver, button_xpath):
    input_first_name = driver.find_element(By.XPATH, "//input[@name='first_name']")
    input_last_name = driver.find_element(By.XPATH, "//input[@name='last_name']")
    input_city = driver.find_element(By.XPATH, "//input[contains(@class,'city')]")
    input_country = driver.find_element(By.XPATH, "//input[@id='country']")
    button = driver.find_element(By.XPATH, button_xpath)

    input_first_name.send_keys("cool")
    input_last_name.send_keys("cool")
    input_city.send_keys("cool")
    input_country.send_keys("cool")
    button.send_keys("cool")

    button.click()


def test_two(driver):

        link = driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
        link.click()
        # test_one(driver)


def test_three():
    try:
        with webdriver.Chrome() as driver:
            driver.get("https://suninjuly.github.io/huge_form.html")

            lst = driver.find_elements(By.XPATH, "//input")
            button = driver.find_element(By.XPATH, "//button")

            for el in lst:
                el.send_keys("cool")

            button.click()
            alert = driver.switch_to.alert
            print(alert.text)
    except NoAlertPresentException as e:
        print(e.msg)


def test_four():
    with webdriver.Chrome() as driver:
        driver.get("https://suninjuly.github.io/find_xpath_form")

        test_one(driver, "//button[text()='Submit']")


def test_five(driver):
    x = driver.find_element(By.XPATH, "//span[@id='input_value']").text
    inp = driver.find_element(By.XPATH, "//input[@id='answer']")
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    radio_button = driver.find_element(By.XPATH, "//label[@for='robotsRule']")
    button = driver.find_element(By.XPATH, "//button[@type='submit']")

    inp.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    checkbox.click()
    driver.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()

    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


def test_six(driver):
    x = driver.find_element(By.XPATH, "//img").get_attribute("valuex")
    inp = driver.find_element(By.XPATH, "//input[@id='answer']")
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    radio_button = driver.find_element(By.XPATH, "//input[@id='robotsRule']")
    button = driver.find_element(By.XPATH, "//button[@type='submit']")

    inp.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    checkbox.click()
    radio_button.click()

    button.click()


def test_seven(driver):
    sum_elements = (int(driver.find_element(By.XPATH, "//span[@id='num1']").text) +
                    int(driver.find_element(By.XPATH, "//span[@id='num2']").text))
    select = Select(driver.find_element(By.XPATH, "//select[@id='dropdown']"))
    select.select_by_value(str(sum_elements))

    driver.find_element(By.XPATH, "//button[@type='submit']").click()


def test_eight(driver):
    file_name = "stepic.py"
    current_path = os.path.abspath(file_name)

    input_first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    lastname = driver.find_element(By.XPATH, "//input[@name='lastname']")
    email = driver.find_element(By.XPATH, "//input[@name='email']")
    upload_file = driver.find_element(By.XPATH, "//input[@name='file']")
    button = driver.find_element(By.XPATH, "//button[@type='submit']")

    input_first_name.send_keys("cool")
    lastname.send_keys("cool")
    email.send_keys("cool")
    upload_file.send_keys(current_path)
    button.click()


def test_nine(driver):
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    alert = driver.switch_to.alert
    alert.accept()
    x = driver.find_element(By.XPATH, "//span[@id='input_value']").text
    inp = driver.find_element(By.XPATH, "//input[@id='answer']")

    inp.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


def test_ten(driver):
    button_magic = driver.find_element(By.XPATH, "//button[@type='submit']")
    button_magic.click()
    driver.switch_to.window(driver.window_handles[1])

    x = driver.find_element(By.XPATH, "//span[@id='input_value']").text
    inp = driver.find_element(By.XPATH, "//input[@id='answer']")

    inp.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


def test_eleven(driver):
    price = WebDriverWait(driver, 15).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), "$100"))
    driver.find_element(By.XPATH, "//button[@id='book']").click()

    x = driver.find_element(By.XPATH, "//span[@id='input_value']").text
    inp = driver.find_element(By.XPATH, "//input[@id='answer']")

    inp.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


start_test("http://suninjuly.github.io/explicit_wait2.html", test_eleven)
