#pip install selenium
#must install chrome web driver

#Simple Google Search

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Search Input
Search = input('What Should I Search?  ')

#Unlocks the browser from code
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

wbrowser = webdriver.Chrome(chrome_options=chrome_options)

#Opens Google in web browser
wbrowser.get("https://google.com") #Can switch out with Bing or Other Search Engine Url bc field name is also 'q'
wbrowser.maximize_window()

#Finds search bar, Enters Search variable in search bar, Submits
input_Element = wbrowser.find_element(By.NAME,'q')
input_Element.send_keys(Search)
input_Element.submit()
