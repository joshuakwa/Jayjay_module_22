import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from assertpy import assert_that


def test_all_filter_on_homepage():
    o = Options()
    o.add_argument("--headless")
    o.add_argument("--start-maximized")
    o.add_argument("--no-sandbox")
    o.add_argument("--ignore-certificate-errors")
    o.add_argument("--disable-gpu")
    o.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=o)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # assert user success login and in homepage
    driver.find_element(By.ID, "item_4_title_link").is_displayed()

    driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    driver.find_element(By.CSS_SELECTOR, "option[value='za']").click()
    text_filter_box = driver.find_element(By.XPATH, "//span[@class='active_option']").text
    assert_that(text_filter_box).is_equal_to("Name (Z to A)")

    driver.find_element(By.CSS_SELECTOR, "option[value='az']").click()
    text_filter_box = driver.find_element(By.XPATH, "//span[@class='active_option']").text
    assert_that(text_filter_box).is_equal_to("Name (A to Z)")

    driver.find_element(By.CSS_SELECTOR, "option[value='lohi']").click()
    text_filter_box = driver.find_element(By.XPATH, "//span[@class='active_option']").text
    assert_that(text_filter_box).is_equal_to("Price (low to high)")

    driver.find_element(By.CSS_SELECTOR, "option[value='hilo']").click()
    text_filter_box = driver.find_element(By.XPATH, "//span[@class='active_option']").text
    assert_that(text_filter_box).is_equal_to("Price (high to low)")

    time.sleep(3)
    driver.quit()
