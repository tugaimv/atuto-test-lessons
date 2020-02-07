from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
	return math.log(abs(12*math.sin(x)))

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/explicit_wait2.html')
	price = WebDriverWait(browser, 15).until(
		EC.text_to_be_present_in_element((By.ID, "price"), '$100') #Задаем явное ожидание 15 секунд или пока в елементе текст не будет равен $100
	)
	browser.find_element(By.ID, 'book').click()
	
	x = browser.find_element_by_id('input_value').text
	result = calc(int(x))
	
	field = browser.find_element_by_id("answer")
	browser.execute_script('return arguments[0].scrollIntoView(true);',field) #Выполнение кастомного js скрипта который проскролит страницу до поля ввода
	field.send_keys(str(result))
	
	browser.find_element(By.ID, 'solve').click()
	
finally:
	time.sleep(3)
	browser.quit()
	