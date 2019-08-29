from selenium import webdriver

driver = webdriver.Chrome("C:/Users/veren_p0omp/Downloads/chromedriver.exe")

# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

# def site_login():
driver.get("https://pr.kargo.tech/shipper/welcome/login")
driver.find_element_by_id("render_phone_number-field").send_keys("82137014747")
driver.find_element_by_id("render_textfield").send_keys("Kargo123")
driver.find_element_by_id("button_component-button").click()

# site_login()