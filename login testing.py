#PROJECT 1--->LOGIN TESTING
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Edge()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.CLASS_NAME, "btn").click()
#moves to dashboard page from login page
logout_btn = driver.find_element(By.LINK_TEXT, "Log out")

assert logout_btn.is_displayed()

print("Successfully logged in")

driver.quit()
#================================================================================================
# #PROJECT 2 -->>  INVALID LOGIN TESTING
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Edge()
# driver.get("https://practicetestautomation.com/practice-test-login/")
# driver.find_element(By.NAME, "username").send_keys("student")
# driver.find_element(By.NAME, "password").send_keys("pass2")
# driver.find_element(By.CLASS_NAME, "btn").click()
# error_msg = driver.find_element(By.ID, "error").text
# msg = error_msg
# assert all(word in msg for word in ['password', 'invalid'])
# print("login not successful")