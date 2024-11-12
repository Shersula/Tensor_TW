from Pages.BasePage import BasePage
from Pages.Sbis.SbisContacts import SbisContacts
from Pages.Sbis.SbisDownload import SbisDownload
from selenium.webdriver.common.by import By

class SbisHomeLocators:
	ContactsBtn = (By.CLASS_NAME, "sbisru-Header__menu-item-1")
	AllContactsLink = (By.PARTIAL_LINK_TEXT, "офис в России")
	LocalVersion = (By.CSS_SELECTOR, "a[href='/download']")

class SbisHome(BasePage):

	def __init__(self, browser):
		super().__init__(browser, "https://sbis.ru/", True)

	def clickOnContacts(self):
		self.find(SbisHomeLocators.ContactsBtn).click()

	def clickOnAllContacts(self):
		URL = self.browser.current_url

		self.find(SbisHomeLocators.AllContactsLink).click()
  
		self.waitUrlChange(URL)
  
		return SbisContacts(self.browser)
	
	def clickOnLocalVersion(self):
		URL = self.browser.current_url

		self.find(SbisHomeLocators.LocalVersion).click()

		self.waitUrlChange(URL)
		
		return SbisDownload(self.browser)
