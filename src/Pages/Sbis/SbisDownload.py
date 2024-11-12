from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class SbisDownloadLocator:
	PluginBtn = (By.CSS_SELECTOR, "div[data-id='plugin']")
	WebDownloadLink = (By.CSS_SELECTOR, "div[data-for='plugin'] div.sbis_ru-DownloadNew-block div:last-child a")

class SbisDownload(BasePage):

	def __init__(self, browser):
		super().__init__(browser, "https://sbis.ru/download")

	def clickPluginBtn(self):
		URL = self.browser.current_url

		self.find(SbisDownloadLocator.PluginBtn).click()

		self.waitUrlChange(URL)

	def getWebDownloadLink(self):
		return self.find(SbisDownloadLocator.WebDownloadLink)