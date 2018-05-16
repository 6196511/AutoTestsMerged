from selenium.webdriver.common.by import By
from webium import BasePage, Find


class ActivityHubPage(BasePage):
    url = 'https://dev.godo.io/activity_hub.aspx'
    add_activity_button = Find(by=By.XPATH, value="//a[@href='activity_information.aspx']//h3[text()='Add Activities']")
    search_activity_field = Find(by=By.XPATH, value="//input[@placeholder='Start typing to search...']")
    activity_title = Find(by=By.XPATH, value="//h2[@class='hub-card-title ng-binding']")
    activity_actions = Find(by=By.XPATH, value="//button[@class='btn btn-primary dropdown-toggle activity-actions-btn']")
    edit_activity = Find(by=By.XPATH, value="//*[@id='activityBG']/div[3]/div[3]/div/div/div[1]/div/div/div[4]/ul/li[2]/a")