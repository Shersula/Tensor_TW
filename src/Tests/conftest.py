import pytest
from selenium import webdriver

@pytest.fixture(scope="class", autouse=True)
def browser(request):
	Service = webdriver.ChromeService(executable_path='Drivers\\yandexdriver.exe')
	request.cls.browser = webdriver.Chrome(service=Service)
	yield
	request.cls.browser.quit()
