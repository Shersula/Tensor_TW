from selenium import webdriver
import pytest
from Pages.Sbis.SbisHome import SbisHome, SbisContacts

class TestScenarioSecond:
	browser : webdriver.Chrome

	def test_region(self):
		self.HomePage = SbisHome(self.browser)
		self.HomePage.clickOnContacts()
		self.ContactPage = self.HomePage.clickOnAllContacts()
		assert ("Нижегородская" in self.ContactPage.getRegion().text)

	def test_contacts(self):
		self.ContactPage = SbisContacts(self.browser)
		Contacts = self.ContactPage.getContacts()

		assert len(Contacts) > 0

	def test_region_change(self):
		self.ContactPage = SbisContacts(self.browser)
		OldContacts = self.ContactPage.getContacts()

		self.ContactPage.clickOnRegionSelectorLink()
		self.ContactPage.clickOnRegionLink(42)
		NewContacts = self.ContactPage.getContacts()

		assert (("Камчатский" in self.ContactPage.getRegionSelectorLink().text)
		  and ("41-kamchatskij" in self.browser.current_url)
		  and len(set(OldContacts) & set(NewContacts)) == 0)
