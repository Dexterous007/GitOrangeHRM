import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
# time.sleep(2)   # Not a standard way to give the time.

# Enter Username
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
# time.sleep(2)   # Not a standard way to give the time.

# Enter Password
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
# time.sleep(2)   # Not a standard way to give the time.

# Click on Login Button
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
# time.sleep(2)   # Not a standard way to give the time.

# Click on "Hien Collings"/Menu
driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
# time.sleep(2)   # Not a standard way to give the time.

# Click on "Logout"
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
# time.sleep(2)   # Not a standard way to give the time.
