import chromedriver_autoinstaller
from selenium import webdriver
from tqdm import tqdm
from selenium.webdriver.common.alert import Alert
from multiprocessing import Pool, cpu_count

# file:///Users/gotaegeon/Documents/Dev/dreamhack/ctf/SecureMail/secure-mail.html
flag = ""

arr = [0, 25, 50, 75]

def find_flag(idx):
  chromedriver_autoinstaller.install()
  options = webdriver.ChromeOptions()
  options.add_argument('headless')

  driver = webdriver.Chrome(options=options)
  driver.implicitly_wait(3)

  driver.get('file:///Users/gotaegeon/Documents/Dev/dreamhack/ctf/SecureMail/secure-mail.html')

  a = driver.find_element_by_xpath('/html/body/input')

  b1 = False
  b2 = False

  for y in tqdm(range(idx, idx + 25)):
    for m in range(13):
      for d in range(32):
        a.send_keys(f'{y}'.zfill(2)+f'{m}'.zfill(2)+f'{d}'.zfill(2))
        driver.find_element_by_xpath('/html/body/button').click()
        da = Alert(driver)

        if da.text == 'Wrong':
          da.accept()
        else:
          global flag
          flag = da.text
          b1 = True
          b2 = True
          print(f'{y}'.zfill(2)+f'{m}'.zfill(2)+f'{d}'.zfill(2))
          break
      if b2:
        break
    if b1:
      break

p = Pool(cpu_count())

queue = p.imap(find_flag, arr)

p.close()
p.join()


print(f"flag is {flag}")