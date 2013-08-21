import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('https://metlifestore.com')
men_apparel_el = driver.find_element_by_xpath('//div[@class="searchline"]/a')

if men_apparel_el:
	men_apparel_el.click()
	time.sleep(5)
product_details_el = driver.find_element_by_xpath('//table[@class="searchTable"]/tbody/tr/td/a')

if product_details_el:
	product_details_el.click()
	time.sleep(3)

# Get title of the product.
product_title_el = driver.find_element_by_xpath('//h3[@class="mainTitle"]')
if product_title_el:
	title = product_title_el.get_attribute('textContent')
	time.sleep(1)

# Get price of the product.
product_price_el = driver.find_element_by_xpath('//div[@class="mainPrice"]')
if product_price_el:
	product_price = product_price_el.get_attribute('textContent')
	time.sleep(1)

# Get description of the product.
description_el = driver.find_element_by_xpath('//p[@class="mainDesc"]')
if description_el:
	description = description_el.get_attribute('textContent').strip()
	time.sleep(1)

# creating the file with crawled result
file = open("extracted_data.txt", "w+")
file.write("Title  : " + title + "\n")
file.write("Price  : " + product_price + "\n")
file.write("Description  : " + description)

driver.close()






