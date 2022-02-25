import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("C:\SeleniumDrivers\chromedriver.exe")

driver = webdriver.Chrome(service=ser)

# maximise browser
driver.maximize_window()


# hyperlink to the website
def land_bt():
    driver.get("https://www.bt.com/products/broadband")
    print(
        '------------------------------------------------------------------------------------------------------------BT DEALS------------------------------------------------------------------------------------------------------------')


# BT cookies hyperlink is not clickable with selenium, so added JS to remove it.
def remove_cookies():
    driver.execute_script("""
       document.querySelectorAll('[class*=overlay]').forEach(element => { element.style.display = 'none' })
    """)


# inserting my postcode to reveal deals available.
def bt_insert_postcode():
    # finding input element that requires post code
    element = driver.find_element(By.XPATH, "//*[@id='sc-postcode']")
    # adding my post code
    element.send_keys("PA1 2JB")
    driver.find_element(By.XPATH, "//*[@id='custom-customer-details']/div/div/form/div/div[2]/div[2]/button").click()
    driver.implicitly_wait(5)
    # clicking address label and search button.
    driver.find_element(By.XPATH, "//*[@id='tvsc-address']/option[2]").click()
    driver.find_element(By.XPATH, "//*[@id='btnCustomConfirmAddress']").click()


# crawling and formating all deals using loop
def bt_products():
    products = driver.find_elements(By.CLASS_NAME, 'jss310')
    print("BT broadband deals today are:")
    for product in products:
        deal_name = product.find_element(By.ID, 'product-name').text
        deal_price = product.find_element(By.ID, 'product-price').text
        deal_speed = product.find_element(By.CLASS_NAME, 'jss1751').text
        deal_set_up_cost = product.find_element(By.CLASS_NAME, 'jss1784').text
        deal_contract_length = product.find_element(By.ID, 'contract-length').text
        print("Name: %s \n Price: %s \n Broadband Speed: %s \n Set up cost: %s \n Contract Length: %s \n " % (
            deal_name, deal_price, deal_speed, deal_set_up_cost, deal_contract_length
        )
              )
        # adding this just to separate all deals
        print(
            '------------------------------------------------------------------------------------------------------------')


def run():
    land_bt()
    time.sleep(3)
    remove_cookies()
    bt_insert_postcode()
    time.sleep(3)
    remove_cookies()
    bt_products()
    driver.quit()
