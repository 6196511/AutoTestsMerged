from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from customer_list import CustomerListPage
from selenium.webdriver.support.ui import Select
import time
import random
from random import choice
from string import digits
from creds import admin_login, admin_password, server, database, username, password
import pyodbc


class BaseTest(object):
    def teardown_class(self):
        close_driver()


class Test_GODO102(BaseTest):
    def test_102(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = CustomerListPage()
        page.open()
        page.add_customer_button.click()
        first_names = ('Ivan', 'Peter', 'John', 'Bill', 'Michael', 'Sidor', 'Alex', 'James', 'Bob', 'Ivan', 'Tim', 'Chris', 'Jim', 'Pahom', 'Vlad', 'Paul')
        NewFirstName = random.choice(first_names)
        page.first_name_field.send_keys(NewFirstName)
        last_names = ('Smith', 'Baker', 'Petroff', 'Smirnoff', 'Black', 'White', 'Broun', 'Ivanoff', 'Green', 'Clinton', 'Jameson', 'Last', 'Sergeff', 'Madison')
        NewLastName = random.choice(last_names)
        NewFullName = NewFirstName+' '+''.join(NewLastName)
        page.last_name_field.send_keys(NewLastName)
        NewPhone= (''.join(choice(digits) for i in range(15)))
        page.phone_field.send_keys(NewPhone)
        NewEmail = (''.join(choice(digits) for i in range(15)) + '@mailinator.com')
        page.email_field.send_keys(NewEmail)
        streets = ('Main Str.', '1St Av.', 'Independence Str', '2nd Str', 'Broadway', 'Bowery', 'Broun', 'Houston Street', 'Maiden Lane', 'Avenue of the Americas')
        NewAddress1 = random.choice(streets)
        page.address1_field.send_keys(NewAddress1)
        NewAddress2 = (''.join(choice(digits) for i in range(3)))
        page.address2_field.send_keys(NewAddress2)
        cities = ('New York', 'Los Angeles', 'Chicago', 'Phoenix', 'San Jose', 'Austin', 'Columbus', 'Charlotte')
        NewCity = random.choice(cities)
        page.city_field.send_keys(NewCity)
        NewZip = (''.join(choice(digits) for i in range(5)))
        page.customer_zip.send_keys(NewZip)
        select = Select(page.country_list)
        NewCountry = 'United States'
        select.select_by_visible_text(NewCountry)
        time.sleep(3)
        select = Select(page.state_list)
        NewState = 'Florida'
        select.select_by_visible_text(NewState)
        time.sleep(5)
        page.save_button.click()
        time.sleep(5)
        page.search_field.send_keys(NewFullName)
        page.search_button.click()
        time.sleep(5)
        assert page.customer_name_in_list.get_attribute('textContent')==NewFullName
        assert page.email_in_list.get_attribute('textContent') == NewEmail
        assert page.phone_in_list.get_attribute('textContent')==NewPhone
        page.edit_button.click()
        assert page.customer_name_info.get_attribute('textContent')==NewFullName+"'s"
        assert page.phone_info.get_attribute('innerText')==NewPhone
        assert page.email_info.get_attribute('innerText') == NewEmail
        assert page.zip_info.get_attribute('innerText')== NewZip
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        cursor.execute("SELECT TOP 1 * FROM customer ORDER BY customer_id DESC")
        row = cursor.fetchone()
        assert row[1]==68 #company ID
        assert row[2]==NewFirstName
        assert row[3]==NewLastName
        assert row[4] == NewAddress1
        assert row[5]==NewAddress2
        assert row[6] == NewCity
        assert row[8] == NewZip
        assert row[10]== NewPhone
        assert row[12] == NewEmail
        assert row[17] == NewEmail #CustomerKey
        assert page.state_info.get_attribute('innerText')==NewState#BUG 2827
        assert page.address_info == NewAddress1+' '+NewAddress2 #BUG 2827
        assert row[9] == 'USA'#BUG 2827
        assert row[7]==NewState#BUG 2827