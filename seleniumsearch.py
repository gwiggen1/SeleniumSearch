#pip install selenium
#must install chrome web driver

#Simple Google Search

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Unlocks the browser from code
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#allows the browser to be independent program (remain open)
wbrowser = webdriver.Chrome(chrome_options=chrome_options)

#Opens Google in web browser
wbrowser.get("https://google.com")
wbrowser.maximize_window()

#Finds search bar, Enters Bing in search bar, Submits
input_Element = wbrowser.find_element(By.NAME,'q')
input_Element.send_keys('Bing')
input_Element.submit()