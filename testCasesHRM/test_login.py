import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Test_Login:


    def test_login_001(self):  # Use Validation here to verify whether Test Case is Failed/Passed.
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # print("Title of the Page: ", driver.title)
        try:              # if found below menu then we say that Test Case is Passed.
            driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
            # login = True
            print("Login Test_001 is Passed")  # after that click on that then click on logout.
            driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
            driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            assert True   # if all done successfully then Passed otherwise  display failed. # PASSED
        except NoSuchElementException:
            # login = False
            print("Login Test_001 is FAiled")  # here we don't use print statement we use here logs.
            assert False                       # logs are maintain instead of print statement.
        print("Test Case is completed successfully")   # Test Case is completed successfully

        """ If enter the wrong credentials the Assertions Error will come"""
        #  AssertionError  # FAILED  ---->>>  Login Test_001 is FAiled


    def test_addEmp_002(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # time.sleep(2)    # take XPATH of PIM Word not mere button.because both XPATH are different.
        driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Aerial")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Rick")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Snow")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(2)
        print(driver.find_element(By.XPATH, "//div[@class='oxd-toast-content oxd-toast-content--success']").text)
        # PASSED   Successfully Saved
        # Now add Validations to check whether it is successful or not.
        try:                             # if found Personal Details then we can say that Test Case is Passed.
            # print(driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']").text)
            driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']")
            # login = True                              # Personal Details
            print("Login Test_001 is Passed")           # after that click on that then click on logout.
            driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
            driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            assert True                  # if all done successfully then Passed otherwise  display failed. # PASSED
        except NoSuchElementException:
            # login = False
            print("Login Test_001 is Failed")             # here we don't use print statement we use here logs.
            assert False                                  # logs are maintain instead of print statement.
        print("Test Case is completed successfully")











