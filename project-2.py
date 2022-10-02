import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Orangehrm:
    driver = webdriver.Chrome()
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)

    def text_login(self):
        username_XPATH = 'input[placeholder="username"]'
        password_XPATH = 'input[type="password"]'
        submit_button_XPATH = 'button[type="submit"]'
        time.sleep(3)

        username_1 = self.driver.find_element(By.XPATH, value=username_XPATH)
        password_1 = self.driver.find_element(By.XPATH, value=password_XPATH)
        submit_button = self.driver.find_element(By.XPATH, value=submit_button_XPATH)

        username_1.send_keys("Admin")
        password_1.send_keys("admin123")
        submit_button.click()
        time.sleep(3)
        print("successfully logged_in")

    def Create_emoloyee(self):
        create_employee = '//div[@class="orangehrm-header-container"]/button[@type=button"]'
        create_employee_1 = self.driver.find_element(by=By.XPATH, value=create_employee)
        create_employee_1.click()
        time.sleep(3)
        print("EmployeeButton clicked")

    def employee_details(self):
        employee_firstname = 'input[name="firstname"]'
        employee_firstname_2 = self.driver.find_element(by=By.CSS_SELECTOR, value=employee_firstname)
        employee_firstname_2.send_keys("Boyana")
        time.sleep(3)
        print("first_name added")

        employee_middlename = '//input[@name="middlename"]'
        employee_middlename_3 = self.driver.find_element(by=By.XPATH, value=employee_middlename)
        employee_middlename_3.send_keys("")
        time.sleep(3)

        employee_lastname = 'input[name="lastname"]'
        employee_lastname_4 = self.driver.find_element(by=By.XPATH, value=employee_lastname)
        employee_lastname_4.send_keys("sunny")
        time.sleep(3)

        employee_id = 'input[@name="ID"]'
        employee_id_5 = self.driver.find_element(by=By.XPATH, value=employee_id)
        employee_id_5.send_keys("4321")
        time.sleep(3)

        employee_firstname_2_XPATH = '//input[@name="orangehrm-firstname"]'
        employee_middlename_3_XPATH = '//input[@name="orangehrm-middlename"]'
        employee_lastaname_4_XPATH = '//input[@type="orangehrm-lastname"]'
        employee_id_5_xpath = '//input[@type=oxd-input-field-button-space"]'

        def text_login_2():
            create_username = '//div[@class="oxd-switch-input-active"]/button[@type=button"]'
            create_username_1 = self.driver.find_element(by=By.XPATH, value=create_username)
            create_username_1.click()
            time.sleep(3)
            print("login activated")

        def create_username():
            create_username = 'input[@name="Boyana sunny"]'
            create_username_2 = self.driver.find_element(by=By.XPATH, value=create_username)
            create_username_2.send_keys("Boyana sunny")
            time.sleep(3)

            create_password = 'input[@name="Bsunny143@"]'
            create_password_3 = self.driver.find_element(by=By.XPATH, value=create_password)
            create_password_3.send_keys("Bsunny143@")
            time.sleep(3)

            create_status = 'input[@name="Enabled"]'
            create_status_4 = self.driver.find_element(by=By.XPATH, value=create_status)
            create_status_4.send_keys("Enabled")
            time.sleep(2)

        def open_Admin():
            open_Admin = '//div[@class="oxd-main-menu-item"]/button[@type=button"]'
            open_Admin = self.driver.find_element(by=By.XPATH, value=open_Admin)
            open_Admin.click()
            time.sleep(2)
            print("AdminButton clicked")

        def system_user():
            username = 'input[@name="oxd-input--active"]'
            username = self.driver.find_element(by=By.XPATH, value=username)
            username.send_keys("Boyana sunny")
            time.sleep(2)

            user_role = 'input[@name="oxd-select-text-input"]'
            user_role = self.driver.find_element(by=By.XPATH, value=user_role)
            user_role.send_keys("Admin")
            time.sleep(2)

            Employee_name = 'input[@name="oxd-autocomplete-text-input-after"]'
            Employee_name = self.driver.find_element(by=By.XPATH, value=Employee_name)
            Employee_name.send_keys("Boyana sunny")
            time.sleep(2)

            Employee_status = 'input[@name="oxd-select-text--action"]'
            Employee_status = self.driver.find_element(by=By.XPATH, value=Employee_status)
            Employee_status.send_keys("Enabled")
            time.sleep(2)

            search_button = '//div[@class="submit"]/button[@type=button"]'
            search_button = self.driver.find_element(by=By.XPATH, value=search_button)
            search_button.click()
            time.sleep(3)
            print("searchButton clicked")

        def about():
            click_button = '//div[@class="oxd-userdropdown-tap"]/button[@type=button"]'
            click_button = self.driver.find_element(by=By.XPATH, value=click_button)
            click_button.send_keys("logout")
            time.sleep(2)
            print("searchButton clicked")

        username_XPATH = 'input[placeholder="username"]'
        password_XPATH = 'input[type="password"]'
        submit_button_XPATH = 'button[type="submit"]'
        time.sleep(3)

        username_1 = self.driver.find_element(By.XPATH, value=username_XPATH)
        password_1 = self.driver.find_element(By.XPATH, value=password_XPATH)
        submit_button = self.driver.find_element(By.XPATH, value=submit_button_XPATH)

        username_1.send_keys("Admin")
        password_1.send_keys("admin123")
        submit_button.click()
        time.sleep(3)
        print("successfully logged_in")

        O= Orangehrm()
        O.text_login()