from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("C:\SeleniumDrivers\chromedriver.exe")

driver = webdriver.Chrome(service=ser)
driver.implicitly_wait(3)
# maximise browser
driver.maximize_window()


# hyperlink to the website
def land_hyperoptic():
    driver.get("https://hyperoptic.com/price-plans/")
    print(
        '------------------------------------------------------------------------------------------------------------HYPEROPRIC DEALS------------------------------------------------------------------------------------------------------------')


# accepting cookies
def accept_cookies():
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '//*[@id="cookiePolicyModal"]/div/div/div[3]/button[1]').click()


# searching and formatting deals. Adding contract length as parameter as it is value that is used to see other deals.
def hyperoptic_deals(deal_contract_length):
    driver.implicitly_wait(3)
    names = ['FAST', 'SUPERFAST', 'ULTRAFAST', 'HYPERFAST']
    name_count = 0
    products = driver.find_elements(By.CLASS_NAME, 'package')
    for product in products:
        deal_name = names[name_count]
        deal_price = product.find_element(By.CLASS_NAME, 'price').text
        deal_price += ' ' + product.find_element(By.CLASS_NAME, 'font-f-museo-700').text
        deal_speed = product.find_element(By.CLASS_NAME, 'size-unit').text
        deal_setup_cost = product.find_element(By.CLASS_NAME, 'font-f-museo-500').text
        print("Name: %s \n Price: %s \n Broadband Speed: %s \n Set up cost: %s \n Contract Length: %s \n " % (
            deal_name, deal_price, deal_speed, deal_setup_cost, deal_contract_length
        )
              )
        name_count += 1
        print(
            '------------------------------------------------------------------------------------------------------------')


# changing to see other deals and changing parameter to a different contract length
def change_deal_length_to_12():
    driver.find_element(By.XPATH, '//*[@id="block_615dba17aa1b4"]/div/div[3]/div/div[2]/div[1]/label[2]').click()
    return driver.find_element(By.XPATH, '//*[@id="block_615dba17aa1b4"]/div/div[3]/div/div[2]/div[1]/label[2]').text


def change_deal_length_to_monthly():
    driver.find_element(By.XPATH, '//*[@id="block_615dba17aa1b4"]/div/div[3]/div/div[2]/div[1]/label[3]').click()
    return driver.find_element(By.XPATH, '//*[@id="block_615dba17aa1b4"]/div/div[3]/div/div[2]/div[1]/label[3]').text


def run():
    land_hyperoptic()
    accept_cookies()
    hyperoptic_deals("24 Months")
    months = change_deal_length_to_12()
    hyperoptic_deals(months)
    months = change_deal_length_to_monthly()
    hyperoptic_deals(months)
    driver.quit()
