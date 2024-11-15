from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
	def __init__(self, browser: webdriver.Chrome, URL, Open = False):
		self.browser: webdriver.Chrome = browser
		self.URL = URL

		if Open: browser.get(URL)
		elif browser.current_url.startswith(URL) == False:
			raise Exception(f"Invalid Page. Expected: {URL} Receive: {browser.current_url}")

	def find(self, locator, delay=5):
		return WebDriverWait(self.browser, delay).until(ec.presence_of_element_located(locator), message="Element not found")
	
	def findAll(self, locator, delay=5):
		return WebDriverWait(self.browser, delay).until(ec.presence_of_all_elements_located(locator), message="Elements not found")
	
	def waitUrlChange(self, Url, delay=5):
		return WebDriverWait(self.browser, delay).until(ec.url_changes(Url))
	
	def waitUrlEqual(self, URL, delay=5):
		return WebDriverWait(self.browser, delay).until(ec.url_to_be(URL))
	
	def waitNewWindow(self, Windows, delay=5):
		return WebDriverWait(self.browser, delay).until(ec.new_window_is_opened(Windows))