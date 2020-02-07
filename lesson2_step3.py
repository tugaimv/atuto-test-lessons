from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/selects1.html')
	num1 = browser.find_element_by_id('num1').text
	num2 = browser.find_element_by_id('num2').text
	result = int(num1) + int(num2)
	
	print(result)
	
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(str(result))
	browser.find_element_by_css_selector('button[type="submit"]').click()
	
finally:
	time.sleep(5)
	browser.quit()