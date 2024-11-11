from Pages.BasePage import BasePage
from Pages.Sbis.SbisContacts import SbisContacts
from selenium.webdriver.common.by import By

class SbisHomeLocators:
	ContactsBtn = (By.CLASS_NAME, "sbisru-Header__menu-item-1")
	AllContactsLink = (By.PARTIAL_LINK_TEXT, "офис в России")

class SbisHome(BasePage):

	def __init__(self, browser):
		super().__init__(browser, "https://sbis.ru/", True)

	def clickOnContacts(self):
		self.find(SbisHomeLocators.ContactsBtn).click()

	def clickOnAllContacts(self):
		self.find(SbisHomeLocators.AllContactsLink).click()
  
		self.waitUrlChange("https:\\/\\/sbis\\.ru\\/contacts\\/.+?\\?tab=clients")
  
		return SbisContacts(self.browser)