from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("file:///C:/Users/intel/Documents/Web%20App/new_page.html")

driver.execute_async_script("var s=window.document.createElement('script'); \
	s.src='file:///C:/Users/intel/Documents/Web%20App/sample_js.js'; \
	window.document.head.appendChild(s);")

