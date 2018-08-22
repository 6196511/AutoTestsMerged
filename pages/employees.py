from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class EmployeePage(BasePage):
    url = 'https://dev.godo.io/administrator.aspx'
    add_new_user = Find(by=By.XPATH, value="//button[@id='addUser']")
    username_field = Find(by=By.XPATH, value="//input[@name='administrator_username']")
    password_field = Find(by=By.XPATH, value="//input[@name='administrator_password']")
    first_name_field = Find(by=By.XPATH, value="//input[@id='administrator_firstname']")
    last_name_field = Find(by=By.XPATH, value="//input[@id='administrator_lastname']")
    phone1_field = Find(by=By.XPATH, value="//input[@id='administrator_phone_1']")
    phone2_field = Find(by=By.XPATH, value="//input[@id='administrator_phone_2']")
    email_field = Find(by=By.XPATH, value="//input[@id='administrator_email']")
    role_list = Find(by=By.XPATH, value="//select[@id='administrator_role']")
    payroll_type_list = Find(by=By.XPATH, value="//select[@id='administrator_payment_type']")
    amount_field = Find(by=By.XPATH, value="//input[@id='administrator_payment_amount']")
    status_checkbox = Find(by=By.XPATH, value="//input[@id='administrator_status']")
    hire_date_field = Find(by=By.XPATH, value="//input[@id='administrator_startdate']")
    end_date_field = Find(by=By.XPATH, value="//input[@id='administrator_enddate']")
    calendar_begin_next = Finds(by=By.XPATH, value="//th[@class='next']")
    calendar_begin_prev = Finds(by=By.XPATH, value="//th[@class='prev']")
    dates_calendar_begin = Finds(by=By.XPATH, value="//td[@class='day']")
    calendar_end_next = Finds(by=By.XPATH, value="//th[@class='next']")
    calendar_end_prev = Finds(by=By.XPATH, value="//th[@class='prev']")
    dates_calendar_end = Finds(by=By.XPATH, value="//td[@class='day']")
    save_button = Find(by=By.XPATH, value="//button[@id='submituser']")
