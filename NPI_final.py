
'''Author: Tom Rafter
Description: Uses Selenium to webscrape an adjacent file containing
a lisk of firstname, last name in an defined array(i.e. providers=[('John','Doe'),('Jane','Doe')])
Wrote this to scape provider NPI #s for a healthcare organization to improve data quality.
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, csv, numpy as np
import list

name=list.providers
state=['CO']
driver = webdriver.Chrome()

def provider_lookup(name):
	for i in range(len(name):
		driver.get("https://npiregistry.cms.hhs.gov/api/demo")
		time.sleep(2)
		elem = driver.find_element_by_name("first_name")
		elem.send_keys(name[i][0])
		elem = driver.find_element_by_name("last_name")
		elem.send_keys(name[i][1])
		elem = driver.find_element_by_name("state")
		elem.send_keys(state)
		elem = driver.find_element_by_name("pretty").click()
		elem=driver.find_element_by_xpath('/html/body/div[1]/form/table/tbody/tr[16]/td[3]/input').click()
		time.sleep(2)
		data = driver.find_element_by_tag_name('body')
		text=data.text
		f=open('npi_all_providers1.txt', 'a')
		f.write('')
		f.write(data.text)
		f.write(', '+'\n')
		f.close()
	driver.close()


provider_lookup(name)


