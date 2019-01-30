from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from customer_list import CustomerListPage
from selenium.webdriver.support.ui import Select
import time
import random
from admin_booking import AdminBookingPage
from navigation_bar import NavigationBar
from dateutil.relativedelta import relativedelta
from event_calendar import EventCalendarPage
from datetime import date, datetime
from creds import admin_login, admin_password, server, database, username, password
from pytz import timezone
import pyodbc


ActivityName = "_AutoTest200918"
ActivityName2 = "AutoTestCustomerKey"
ActivityTimezone = 'AT'
ActivityTimezone2 = 'PT'
AdultTickets = '1'
AdultTicketPrice = '$0.90'
AdultTicketPrice2 = '$100.00'
AT = timezone('America/Glace_Bay')
PT = timezone('America/Los_Angeles')



class BaseTest(object):
    def teardown_class(self):
        close_driver()


class Test_GODO884(BaseTest):
    def test_884(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = NavigationBar()
        time.sleep(2)
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click() #STEP1
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(ActivityName)#STEP2
        page.first_tickets_type.send_keys(AdultTickets) #STEP3
        time.sleep(5)
        page.datepicker_next_month.click()
        time.sleep(5)
        EventDate = str(random.randint(2, 27)) #STEP4
        for i in range(0, len(page.dates)):
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = str(random.randint(2, 11))
        minutes_values = ('00', '15', '30', '45')
        EventTimeMinutes = random.choice(minutes_values)
        timeday = random.choice(('AM', 'PM'))
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(
            ActivityTimezone))
        nextMonthDate = (datetime.now() + relativedelta(months=1)).strftime('%#m')
        NextMonthName = (datetime.now() + relativedelta(months=1)).strftime("%B")
        NewFullDate = (NextMonthName + ' ' + ''.join(str(EventDate)))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone) #STEP5
        time.sleep(5)
        page.enter_customer_information_button.click() #STEP6
        first_names = (
        'Ivan-John', 'Peter-Paul', 'John-Alex', 'Bill-Michael', 'Michael-James', 'Sidor-Bob', 'Alex-Ivan', 'James-Tim', 'Bob-Chris', 'Ivan-Jim', 'Tim-Michael', 'Chris-Jim', 'Jim-John',
        'Pahom-Sidor', 'Vlad-Vadim', 'Paul-James')
        NewFirstName = random.choice(first_names)
        page.first_name.send_keys(NewFirstName) #STEP7
        last_names = (
        'Smith', 'Baker', 'Petroff', 'Smirnoff', 'Black', 'White', 'Broun', 'Ivanoff', 'Green', 'Clinton', 'Jameson',
        'Last', 'Sergeff', 'Madison')
        NewLastName = random.choice(last_names)
        NewFullName = NewFirstName + ' ' + ''.join(NewLastName)
        page.last_name.send_keys(NewLastName)
        page.complete_booking_button.click()
        time.sleep(7)
        select = Select(page.payment_type_list)
        PaymentType = "Cash" #STEP8
        select.select_by_visible_text(PaymentType)
        page.cash_recieved.click()
        page.submit_booking_button.click()
        time.sleep(5)
        page = EventCalendarPage() #STEP10
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(ActivityName)
        page.date_picker.click()
        time.sleep(2)
        page.date_picker_next.click()
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(EventDate):
                page.days_date_picker[i].click()
            else:
                continue
            break
        page.day_button.click()
        time.sleep(6)
        EventTime = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday))
        assert str(NewFullDate) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots: #STEP11
            for i in range(0, len(page.day_slots)):
                if EventTime in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                else:
                    continue
            break
        time.sleep(6)
        assert page.customer_name_link.get_attribute('textContent')==NewFullName
        page.customer_name_link.click()  # STEP12
        page = CustomerListPage()
        assert page.customer_name_info.get_attribute('textContent')==NewFullName+"'s"
        #assert page.phone_info.get_attribute('innerText')=='Not Saved' #BUG 2954
        assert page.email_info.get_attribute('innerText') == 'Not Saved'
        assert page.zip_info.get_attribute('innerText')== 'Not Saved'
        assert page.state_info.get_attribute('innerText')=='Not Saved'
        assert page.address_info.get_attribute('innerText') == 'Not Saved'
        assert page.timeline_tickets_title.get_attribute('textContent') == 'Purchased Tickets for the '+''.join(ActivityName)
        assert EventTimeWithZone and NewFullDate in page.timeline_event.get_attribute('textContent')
        assert page.timeline_tickets.get_attribute('textContent') == AdultTickets+' Tickets | ' +''.join(AdultTicketPrice)+' '
        page.activities_tab_link.click()
        time.sleep(5)
        assert page.activities_tab_title.get_attribute('innerText') == ActivityName
        assert page.activities_tickets.get_attribute('innerText') == AdultTickets + ' tickets | ' + ''.join(AdultTicketPrice)
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password) #STEP 14
        cursor = cnxn.cursor()
        cursor.execute("SELECT TOP 1 * FROM customer ORDER BY customer_id DESC")
        row = cursor.fetchone()
        CustomerID = row[0]
        assert row[1]==68 #company ID
        assert row[2]==NewFirstName
        assert row[3]==NewLastName
        assert row[4] == None #customer_address_1
        assert row[5] == None #customer_address_2
        assert row[6] == None #customer_city
        assert row[7] == None #customer_state
        assert row[8] == None #customer_zipcode
        assert row[9] == None #customer_country
        assert row[10] == None #customer_phone_1
        assert row[11] == None #customer_phone_2
        assert row[12] == None #customer_email
        assert row[17] == None #CustomerKey
        page = NavigationBar()
        time.sleep(2)
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click()  # STEP15
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(ActivityName2)  # STEP16
        page.first_tickets_type.send_keys(AdultTickets)  # STEP17
        time.sleep(5)
        page.datepicker_next_month.click()
        time.sleep(5)
        EventDate = str(int(EventDate)+1)  # STEP18
        for i in range(0, len(page.dates)):
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = str(random.randint(2, 11))
        minutes_values = ('00', '15', '30', '45')
        EventTimeMinutes = random.choice(minutes_values)
        timeday = random.choice(('AM', 'PM'))
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(
            ActivityTimezone2))
        NextMonthName = (datetime.now() + relativedelta(months=1)).strftime("%B")
        NewFullDate = (NextMonthName + ' ' + ''.join(str(EventDate)))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone)  # STEP19
        time.sleep(5)
        page.enter_customer_information_button.click()  # STEP20
        page.first_name.send_keys(NewFirstName)  # STEP21
        page.last_name.send_keys(NewLastName)
        page.complete_booking_button.click()
        time.sleep(7)
        select = Select(page.payment_type_list)
        PaymentType = "Cash"  # STEP22
        select.select_by_visible_text(PaymentType)
        page.cash_recieved.click()
        page.submit_booking_button.click()
        time.sleep(5)
        page = EventCalendarPage()  # STEP24
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(ActivityName2)
        page.date_picker.click()
        time.sleep(2)
        page.date_picker_next.click()
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(EventDate):
                page.days_date_picker[i].click()
            else:
                continue
            break
        page.day_button.click()
        time.sleep(6)
        EventTime = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday))
        assert str(NewFullDate) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:  # STEP25
            for i in range(0, len(page.day_slots)):
                if EventTime in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                else:
                    continue
            break
        time.sleep(6)
        assert page.customer_name_link.get_attribute('textContent') == NewFullName
        page.customer_name_link.click()  # STEP26
        page = CustomerListPage()
        assert page.customer_name_info.get_attribute('textContent') == NewFullName + "'s"
        # assert page.phone_info.get_attribute('innerText')=='Not Saved' #BUG 2954
        assert page.email_info.get_attribute('innerText') == 'Not Saved'
        assert page.zip_info.get_attribute('innerText') == 'Not Saved'
        assert page.state_info.get_attribute('innerText') == 'Not Saved'
        assert page.address_info.get_attribute('innerText') == 'Not Saved'
        assert page.timeline_tickets_title.get_attribute('textContent') == 'Purchased Tickets for the ' + ''.join(
            ActivityName2)
        assert EventTimeWithZone and NewFullDate in page.timeline_event.get_attribute('textContent')
        assert page.timeline_tickets.get_attribute('textContent') == AdultTickets + ' Tickets | ' + ''.join(
            AdultTicketPrice2) + ' '
        page.activities_tab_link.click()  # STEP27
        time.sleep(5)
        assert page.activities_tab_title.get_attribute('innerText') == ActivityName2
        assert page.activities_tickets.get_attribute('innerText') == AdultTickets + ' tickets | ' + ''.join(
            AdultTicketPrice2)
        page = CustomerListPage() # STEP28
        page.open()
        page.search_field.send_keys(NewFullName)
        page.search_button.click()
        time.sleep(2)
        assert page.customer_name_in_list.get_attribute('textContent') == NewFullName
        assert page.customer_name_in_list2.get_attribute('textContent') == NewFullName
        assert page.activity_name_in_list.get_attribute('textContent') == ActivityName2
        assert page.activity_name_in_list2.get_attribute('textContent') == ActivityName
        cursor.execute("SELECT TOP 1 * FROM customer ORDER BY customer_id DESC")
        row = cursor.fetchone()
        assert row[0]==CustomerID+1
        assert row[1]==68 #company ID
        assert row[2]==NewFirstName
        assert row[3]==NewLastName
        assert row[4] == None #customer_address_1
        assert row[5] == None #customer_address_2
        assert row[6] == None #customer_city
        assert row[7] == None #customer_state
        assert row[8] == None #customer_zipcode
        assert row[9] == None #customer_country
        assert row[10] == None #customer_phone_1
        assert row[11] == None #customer_phone_2
        assert row[12] == None #customer_email
        assert row[17] == None #CustomerKey
        cursor.execute("SELECT * FROM customer ORDER BY customer_id DESC OFFSET 1 ROWS FETCH NEXT 1 ROW ONLY")
        row = cursor.fetchone()
        assert row[0]==CustomerID
        assert row[1]==68 #company ID
        assert row[2]==NewFirstName
        assert row[3]==NewLastName
        assert row[4] == None #customer_address_1
        assert row[5] == None #customer_address_2
        assert row[6] == None #customer_city
        assert row[7] == None #customer_state
        assert row[8] == None #customer_zipcode
        assert row[9] == None #customer_country
        assert row[10] == None #customer_phone_1
        assert row[11] == None #customer_phone_2
        assert row[12] == None #customer_email
        assert row[17] == None #CustomerKey