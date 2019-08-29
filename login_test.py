from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        

import time 

driver = webdriver.Chrome("C:/Users/veren_p0omp/Downloads/chromedriver.exe")

def site_login():
    driver.get("https://pr.kargo.tech/shipper/welcome/login")
    driver.find_element_by_id("render_phone_number-field").send_keys("82137014747")
    driver.find_element_by_id("render_textfield").send_keys("Kargo123")
    driver.find_element_by_id("button_component-button").click()
    time.sleep(10)
    url = driver.current_url
    if (url == "https://pr.kargo.tech/shipper/welcome/home"):
        print("login done")
    driver.quit()

def test_no_phone():
    driver.get("https://pr.kargo.tech/shipper/welcome/login")
    driver.find_element_by_id("render_textfield").click()
    try:
        driver.find_elements_by_xpath("//*[contains(text(), 'Masukkan nomor telepon')]")
    except NoSuchElementException:
        return False
    return True

def test_no_password():
    driver.get("https://pr.kargo.tech/shipper/welcome/login")
    driver.find_element_by_id("render_textfield").click()
    driver.find_element_by_tag_name('body').click()
    try:
        driver.find_elements_by_xpath("//*[contains(text(), 'Masukkan password')]")
    except NoSuchElementException:
        return False
    return True

if (test_no_phone()):
    print ("test no phone done")
else:
    print ("test no phone failed")

if (test_no_password()):
    print ("test no password done")
else:
    print ("test no password failed")

site_login()