from Pages.BasePage import BasePage
from Pages.Tensor.TensorHome import TensorHome
from selenium.webdriver.common.by import By

class SbisContactsLocator:
	TensorLogo = (By.CSS_SELECTOR, "div#contacts_clients a.sbisru-Contacts__logo-tensor")
	Region = (By.CSS_SELECTOR, "div.sbis_ru-container.sbisru-Contacts__relative span.sbis_ru-Region-Chooser__text.sbis_ru-link")
	Contacts = (By.CSS_SELECTOR, "div#contacts_list div[item-parent-key='-2'] div.sbisru-Contacts-List__name")
	RegionSelectorLink = (By.CSS_SELECTOR, "div.sbis_ru-container.sbisru-Contacts__relative span.sbis_ru-Region-Chooser")
	RegionLink = (By.CSS_SELECTOR, f"ul.sbis_ru-Region-Panel__list-l li")

class SbisContacts(BasePage):
	def __init__(self, browser):
		super().__init__(browser, "https://sbis.ru/contacts")

	def clickOnTensorLogo(self):
     
		OldHandles = self.browser.window_handles
     
		self.find(SbisContactsLocator.TensorLogo).click()
  
		self.waitNewWindow(OldHandles)
		self.browser.switch_to.window([w for w in self.browser.window_handles if w not in OldHandles][0])
		
		return TensorHome(self.browser)
	
	def getRegion(self):
		return self.find(SbisContactsLocator.Region)
	
	def getContacts(self):
		return self.findAll(SbisContactsLocator.Contacts)
	
	def getRegionSelectorLink(self):
		return self.find(SbisContactsLocator.RegionSelectorLink)

	def clickOnRegionSelectorLink(self):
		self.getRegionSelectorLink().click()

	def clickOnRegionLink(self, li_number):
		URL = self.browser.current_url
		self.findAll(SbisContactsLocator.RegionLink)[li_number].click()
		self.waitUrlChange(URL)