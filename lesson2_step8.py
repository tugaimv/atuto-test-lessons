from selenium import webdriver
import os
import time

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file_for_test.txt')

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/file_input.html')
	browser.find_element_by_css_selector("input[required][name='firstname']").send_keys('hello')
	browser.find_element_by_css_selector("input[required][name='lastname']").send_keys('hello')
	browser.find_element_by_css_selector("input[required][name='email']").send_keys('hello')
	
	buttonUpload = browser.find_element_by_id("file")
	buttonUpload.send_keys(file_path)

	button = browser.find_element_by_css_selector("button[type='submit']")
	button.click()
finally:
	time.sleep(5)
	browser.quit()