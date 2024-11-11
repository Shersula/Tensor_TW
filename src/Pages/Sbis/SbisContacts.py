from Pages.BasePage import BasePage
from Pages.Tensor.TensorHome import TensorHome
from selenium.webdriver.common.by import By

class SbisContactsLocator:
	TensorLogo = (By.CSS_SELECTOR, "div#contacts_clients a.sbisru-Contacts__logo-tensor")

class SbisContacts(BasePage):
	def __init__(self, browser):
		super().__init__(browser, "https://sbis.ru/contacts")

	def clickOnTensorLogo(self):
     
		OldHandles = self.browser.window_handles
     
		self.find(SbisContactsLocator.TensorLogo).click()
  
		self.waitNewWindow(OldHandles)
		self.browser.switch_to.window([w for w in self.browser.window_handles if w not in OldHandles][0])
		
		return TensorHome(self.browser)