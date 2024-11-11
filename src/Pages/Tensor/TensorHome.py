from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Pages.Tensor.TensorAbout import TensorAbout

class TensorHomeLocator:
    TeamBlockTitle = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-bg p.tensor_ru-Index__card-title")
    TeamBlockAboutBtn = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-bg a.tensor_ru-link.tensor_ru-Index__link")

class TensorHome(BasePage):
	def __init__(self, browser):
		super().__init__(browser, "https://tensor.ru/")
	
	def getTeamBlockTitle(self):
		return self.find(TensorHomeLocator.TeamBlockTitle)

	def clickTeamBlockAboutBtn(self):
		self.find(TensorHomeLocator.TeamBlockAboutBtn).click()
		self.waitUrlEqual("https://tensor.ru/about")

		return TensorAbout(self.browser)