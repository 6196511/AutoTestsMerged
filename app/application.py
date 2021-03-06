import webium.settings
from selenium import webdriver

from actions.activity_hub import ActivityHub
from actions.addons import Addons
from actions.admin_booking import AdminBooking
from actions.calendar import Calendar
from actions.certificate import CertificateActions
from actions.customer_booking import CustomerActions
from actions.customer_certificate import CustomerCertActions
from actions.groupons import Groupons
from actions.people_hub import PeopleHub
from actions.rain_checks import RainChecks
from actions.waiting import Waiting
from app.session import SessionHelper


class Application:

    def __init__(self, browser, domain, credentials):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser {}".format(browser))
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.set_script_timeout(30)
        self.driver.set_page_load_timeout(60)
        webium.settings.wait_timeout = 15
        self.session = SessionHelper(self, domain, credentials)
        self.customer_booking = CustomerActions(self, domain=domain)
        self.customer_certs = CustomerCertActions(self, domain=domain)
        self.booking = AdminBooking(self)
        self.certificate = CertificateActions(self)
        self.activity_hub = ActivityHub(self)
        self.people_hub = PeopleHub(self)
        self.groupons = Groupons(self)
        self.addons = Addons(self)
        self.calendar = Calendar(self)
        self.rain_checks = RainChecks(self)
        self.waiting = Waiting(self)

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.current_url()
            return True
        except:
            return False

    def current_url(self):
        return self.driver.current_url

    def refresh_page(self):
        menu = self.session.navigation_bar.main_tab
        self.driver.refresh()
        self.waiting.for_staleness(element=menu, timeout=5)
