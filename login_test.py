from selenium import webdriver
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
        print("done")

site_login()

def test_no_phone():
    driver.get("https://pr.kargo.tech/shipper/welcome/login")
    driver.find_element_by_id("button_component-button").click()
    a = driver.find_elements_by_xpath("//*[contains(text(), 'Masukkan nomor telepon')]")

# test_no_phone()