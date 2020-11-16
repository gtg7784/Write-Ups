from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://www.naver.com")

da = Alert(driver)