from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import chromedriver_autoinstaller

# file:///Users/gotaegeon/Documents/Dev/dreamhack/ctf/SecureMail/secure-mail.html

chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

driver.get('file:///Users/gotaegeon/Documents/Dev/dreamhack/ctf/SecureMail/secure-mail.html')

a = driver.find_element_by_xpath('/html/body/input')

b1 = False
b2 = False

for y in range(50, 100):
  for m in range(13):
    for d in range(32):
      print(f'{y}'.zfill(2)+f'{m}'.zfill(2)+f'{d}'.zfill(2))
      a.send_keys(f'{y}'.zfill(2)+f'{m}'.zfill(2)+f'{d}'.zfill(2))
      driver.find_element_by_xpath('/html/body/button').click()
      da = Alert(driver)

      if da.text == 'Wrong':
        da.accept()
      else:
        print(da.text)
        b1 = True
        b2 = True
        break
    if b2:
      break
  if b1:
    break