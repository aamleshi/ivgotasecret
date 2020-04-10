from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/NYUSecrets/")
# assert "Python" in driver.title
time.sleep(3)
#elem = driver.find_element_by_name("_4bl9")

texts = driver.find_elements_by_class_name('_4bl9')
for text in texts[2:5]:
    print(text.text)
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()
