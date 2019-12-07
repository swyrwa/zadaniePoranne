# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
from datetime import time

from selenium import webdriver
from selenium.webdriver.support import select

driver = webdriver.Chrome()
driver.get("https://www.google.pl/")
driver.maximize_window()
driver.implicitly_wait(5)
elem = driver.find_element_by_name("q")
elem.send_keys("CDV")
elem.submit()
elem = driver.find_element_by_name("q")
elem.click()
dropdown = select.first_selected_option()
# elem.clear()
# driver.close()

