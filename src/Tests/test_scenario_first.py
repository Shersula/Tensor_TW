import pytest
from Pages.Sbis.SbisHome import SbisHome
from Pages.Tensor.TensorHome import TensorHome, TensorAbout

class TestScenarioFirst:

	def test_team_title(self):
		self.HomePage = SbisHome(self.browser)
		self.HomePage.clickOnContacts()
		self.ContactPage = self.HomePage.clickOnAllContacts()

		self.TensorHomePage = self.ContactPage.clickOnTensorLogo()

		try:
			self.TensorHomePage.getTeamBlockTitle()
		except: assert False
		else: assert True
  
	def test_tensor_about_link(self):
		self.TensorHomePage = TensorHome(self.browser)
		
		try:
			self.TensorHomePage.clickTeamBlockAboutBtn()
		except: assert False
		else: assert True

	def test_tensor_about_img_size(self):
		self.TensorAboutPage = TensorAbout(self.browser)
		ImgList = self.TensorAboutPage.getWorkBlockImg()

		Width, Height = None, None

		for i in ImgList:
			if Width == None and Height == None:
				Width = i.get_attribute("width")
				Height = i.get_attribute("height")
			elif i.get_attribute("width") != Width or i.get_attribute("height") != Height: assert False

		assert True