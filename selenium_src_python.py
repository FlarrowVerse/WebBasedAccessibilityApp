from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import io

driver = webdriver.Firefox()
driver.get("https://www.google.com")

elem = driver.find_element_by_xpath("//*")
src_code = elem.get_attribute("innerHTML")

filename = io.open('google_home.html', 'w', encoding='utf8')
filename.write(src_code)

sleep(10)

driver.close()