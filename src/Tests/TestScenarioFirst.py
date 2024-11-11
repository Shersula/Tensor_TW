import pytest
from selenium import webdriver
from Pages.Sbis.SbisHome import SbisHome
from Pages.Tensor.TensorHome import TensorHome

class TestScenarioFirst:

	@classmethod
	def setup_class(cls):
		Service = webdriver.ChromeService(executable_path='Drivers\\yandexdriver.exe')
		cls.driver = webdriver.Chrome(service=Service)

	@classmethod
	def teardown_class(cls):
		cls.driver.quit()

	@classmethod
	def test_team_title(cls):
		cls.HomePage = SbisHome(cls.driver)
		cls.HomePage.clickOnContacts()
		cls.ContactPage = cls.HomePage.clickOnAllContacts()

		cls.TensorHomePage = cls.ContactPage.clickOnTensorLogo()

		try:
			cls.TensorHomePage.getTeamBlockTitle()
		except: assert False
		else: assert True
  
	@classmethod
	def test_tensor_about_link(cls):
		try:
			cls.TensorAboutPage = cls.TensorHomePage.clickTeamBlockAboutBtn()
		except: assert False
		else: assert True

	@classmethod
	def test_tensor_about_img_size(cls):
		ImgList = cls.TensorAboutPage.getWorkBlockImg()

		Width, Height = None, None

		for i in ImgList:
			if Width == None and Height == None:
				Width = i.get_attribute("width")
				Height = i.get_attribute("height")
			elif i.get_attribute("width") != Width or i.get_attribute("height") != Height: assert False

		assert True