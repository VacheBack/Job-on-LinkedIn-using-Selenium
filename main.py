from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "grigoryanvache10.01@yahoo.com"
ACCOUNT_PASSWORD = "Vachebest123-"
LOCATION = "Yerevan, Yerevan, Armenia"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3969657219&f_LF=f_AL&geoId=102475833&keywords=python%20developer&location=Yerevan%2C%20Armenia&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

time.sleep(2)
reject_button = driver.find_element(By.XPATH, value='//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]')
reject_button.click()

time.sleep(2)
signin_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
signin_button.click()

email = driver.find_element(By.ID, value="username")
email.send_keys(ACCOUNT_EMAIL)

email = driver.find_element(By.ID, value="password")
email.send_keys(ACCOUNT_PASSWORD)

signin_button1 = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
# XPATH always get changed, so we can use "contain(text(), 'The text') function in value to find the exact XPATH"
signin_button1.click()

time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

time.sleep(4)
next_button = driver.find_element(By.CSS_SELECTOR, value='footer div button')
next_button.click()

time.sleep(4)
next_button = driver.find_element(By.CLASS_NAME, value='artdeco-button artdeco-button--2 artdeco-button--primary ember-view')
next_button.click()