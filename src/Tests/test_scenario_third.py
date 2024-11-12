import os, re
from selenium import webdriver
import pytest, requests
from Pages.Sbis.SbisHome import SbisHome, SbisContacts

class TestScenarioThird:
	browser : webdriver.Chrome

	def test_download(self):
		self.HomePage = SbisHome(self.browser)
		self.DownloadPage = self.HomePage.clickOnLocalVersion()
		if "tab=plugin" in self.browser.current_url == False: self.DownloadPage.clickPluginBtn()
		
		DownloadLink = self.DownloadPage.getWebDownloadLink()
		DownloadText = DownloadLink.text
		
		Dimension : str
		for s in re.compile("[а-яА-я]+").finditer(DownloadText): Dimension = s.group()
		Size = float(re.compile("[\\d\\.]+").findall(DownloadText)[0])

		if os.path.exists('download') == False: os.mkdir('download')
		outfile = os.path.join('download', 'web_installer.exe')

		response = requests.get(DownloadLink.get_attribute('href'), stream=True)

		with open(outfile, 'wb') as output:
			output.write(response.content)

		OutputSize : float = float(os.path.getsize(outfile))

		if "КБ" in Dimension.upper():
			OutputSize = OutputSize/1024.0
		elif "МБ" in Dimension.upper():
			OutputSize = OutputSize/pow(1024.0, 2)
		elif "ГБ" in Dimension.upper():
			OutputSize = OutputSize/pow(1024.0, 3)

		assert round(Size, 2) == round(OutputSize, 2)