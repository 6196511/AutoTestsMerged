from selenium.webdriver.common.by import By
from webium import BasePage, Find


class ActivityHubPage(BasePage):
    url = 'https://ci004.godo.io/activity_hub.aspx'
    add_activity_button = Find(by=By.XPATH, value="//a[@href='activity_information.aspx']//h3[text()='Add Activities']")
    addons_button = Find(by=By.XPATH, value="//h3[text()='Add-Ons']")
    search_activity_field = Find(by=By.XPATH, value="//input[@placeholder='Start typing to search...']")
    activity_title = Find(by=By.XPATH, value="//h2[@class='hub-card-title ng-binding']")
    activity_actions = Find(by=By.XPATH, value="//div[contains(@class, 'card-body')]//button")
    edit_activity = Find(by=By.XPATH, value="//div[contains(@class, 'card-body')]//a[text()='Edit Activity']")
    add_events = Find(by=By.XPATH, value="//i[@class='fa fa-plus mr20']")
    get_widget = Find(by=By.XPATH, value="//i[@class='fa fa-code mr20']")
    view_calendar = Find(by=By.XPATH, value="//i[@class='fa fa-calendar mr20']")
    show_inactive = Find(by=By.XPATH, value="//*[@id='activityBG']/div[3]/div[2]/div/div/label")
    add_location_button = Find(by=By.XPATH, value="//a[@href='location_information.aspx']//h3[text()='Locations']")
