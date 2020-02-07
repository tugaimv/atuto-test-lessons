from selenium import webdriver
import math
import time

def calc(x):
	return math.log(abs(12*math.sin(x)))

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/alert_accept.html')
	
	button1 = browser.find_element_by_css_selector("button[type='submit']")
	button1.click()
	browser.switch_to.alert.accept() #нажатие кнопки ОК в алерте 
	time.sleep(1)
	
	x = browser.find_element_by_id('input_value').text
	result = calc(int(x))
	
	browser.find_element_by_id('answer').send_keys(str(result))
	
	
	button = browser.find_element_by_css_selector("button[type='submit']")
	button.click()
finally:
	time.sleep(5)
	browser.quit()