from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/math.html')
	x_element = browser.find_element_by_id('input_value')
	x = x_element.text
	y = calc(x)
	browser.find_element_by_id('answer').send_keys(y)
	browser.find_element_by_id('robotCheckbox').click()
	browser.find_element_by_id('robotsRule').click()
	browser.find_element_by_css_selector('button[type="submit"]').click()
finally:
	time.sleep(5)
	browser.quit()