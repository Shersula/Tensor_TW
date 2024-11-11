from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class TensorAboutLocator:
	WorkBlockImg = (By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 img")

class TensorAbout(BasePage):
	def __init__(self, browser):
		super().__init__(browser, "https://tensor.ru/about")

	def getWorkBlockImg(self):
		return self.findAll(TensorAboutLocator.WorkBlockImg)