from webium import BasePage, Find, Finds
from selenium.webdriver.common.by import By


class ChannelPage(BasePage):
    url = 'https://ci004.godo.io/channel.aspx'
    add_channel_button = Find(by=By.XPATH, value="//button[@id='addChannel']")
    username_field = Find(by=By.XPATH, value="//input[@ng-model='vm.channel.username']")
    password_field = Find(by=By.XPATH, value="//input[@ng-model='vm.channel.password']")
    channel_name = Find(by=By.XPATH, value="//input[@id='channel_name']")
    first_name_field = Find(by=By.XPATH, value="//input[@id='channel_firstname']")
    last_name_field = Find(by=By.XPATH, value="//input[@id='channel_lastname']")
    house_number_field = Find(by=By.XPATH, value="//input[@id='channel_address_1']")
    street_field = Find(by=By.XPATH, value="//input[@id='channel_address_2']")
    country_list = Find(by=By.XPATH, value="//select[@id='channel_country']")
    state_list = Find(by=By.XPATH, value="//select[@id='channel_state']")
    city_field = Find(by=By.XPATH, value="//input[@id='channel_city']")
    zip_code = Find(by=By.XPATH, value="//input[@id='channel_zipcode']")
    phone1_field = Find(by=By.XPATH, value="//input[@id='channel_phone_1']")
    phone2_field = Find(by=By.XPATH, value="//input[@id='channel_phone_2']")
    email_field = Find(by=By.XPATH, value="//input[@id='channel_email']")
    comission_type_list = Find(by=By.XPATH, value="//select[@ng-model='vm.selectedCommissionType']")
    comission_amount = Find(by=By.XPATH, value="//input[@id='channel_commission']")
    bank_name_field = Find(by=By.XPATH, value="//input[@id='channel_bank_name']")
    bank_account_type = Find(by=By.XPATH, value="//select[@id='channel_bank_type']")
    routing_number_field = Find(by=By.XPATH, value="//input[@id='channel_bank_routingnumber']")
    account_number_field = Find(by=By.XPATH, value="//input[@id='channel_bank_accountnumber']")
    status_checkbox = Find(by=By.XPATH, value="//input[@ng-model='vm.channel.isActive']")
    save_button = Find(by=By.XPATH, value="//button[@id='btnsave']")
    cancel_button = Find(by=By.XPATH, value="//button[@ng-click='vm.cancel()']")
    search_field = Find(by=By.XPATH, value="//input[@type='search']")
    table_channel_name = Find(by=By.XPATH, value="//*[@id='dtChannel']/tbody/tr/td[1]")
    table_channel_comission = Find(by=By.XPATH, value="//*[@id='dtChannel']/tbody/tr/td[2]")
    table_channel_phonenumber = Find(by=By.XPATH, value="//*[@id='dtChannel']/tbody/tr/td[3]")
    table_channel_email = Find(by=By.XPATH, value="//*[@id='dtChannel']/tbody/tr[1]/td[4]")
    table_channel_editbutton = Find(by=By.XPATH, value="//i[@class='fa fa-edit']")
    table_channel_delete_button = Find(by=By.XPATH, value="//i[@class='fa fa-remove']")
    table_empty = Find(by=By.XPATH, value="//td[@class='dataTables_empty']")
    table_entries_qty = Find(by=By.XPATH, value="//div[@id='dtChannel_info']")
    channel_exist_alert = Find(by=By.XPATH, value="//div[@class='modal-body ng-binding']")
    OK_alert = Find(by=By.XPATH, value="//button[@ng-click='vm.cancel()']")
