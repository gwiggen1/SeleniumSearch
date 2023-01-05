# SeleniumSearch
Fast Google Search W Selenium

### Requirements:
[Chromedriver](https://chromedriver.chromium.org/downloads)
```
pip install Selenium
```


### Detaching the Chromedriver from Python(This makes Chrome stay open after the program runs): 
```
#Required import for following code
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Unlocks the browser from code
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

wbrowser = webdriver.Chrome(chrome_options=chrome_options)
```
### Input:

You will have to input your search in the command line:

![Selenium](https://user-images.githubusercontent.com/121186555/210836557-356b771a-e518-400e-999a-32e4d3ac0995.PNG)
