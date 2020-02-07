from selenium import webdriver
import math
import time
def calc(x):
	return math.log(abs(12*math.sin(x)))

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/execute_script.html')
	x = browser.find_element_by_id('input_value').text
	result = calc(int(x))
	button = browser.find_element_by_css_selector("button[type='submit']")
	field = browser.find_element_by_id("answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", field)
	field.send_keys(str(result))
	browser.find_element_by_id("robotCheckbox").click()
	browser.find_element_by_id("robotsRule").click()
	
	button.click()
finally:
	time.sleep(5)
	browser.quit()