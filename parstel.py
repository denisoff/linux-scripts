# 
import time 
from datetime import datetime, date
import string
import re
import selenium
import json
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
jpage=""
url = '' # link to site
# here and further is site xpath
login=""
passw=""
button=""
dashboard=""
# create useragent
ua = UserAgent()
options = Options()
options.add_argument('--headless=new')
options.add_argument(f'user-agent={ua.chrome}')
driver = webdriver.Chrome(options=options)
driver.get(url) # get page for chrome headless
time.sleep(2) # loading time 
driver.find_element(By.XPATH, value=login).send_keys('')
driver.find_element(By.XPATH, value=passw).send_keys('')
driver.find_element(By.XPATH, value=button).click()
time.sleep(2)
page = driver.find_element(By.XPATH, value=dashboard).text # save page text to variable
# close session Chrome headless and quit
driver.close() 
driver.quit()
# replace need strings
page = page.replace("user\ntelephone\ngroups\nCall back\n","")
page = page.replace("queue\n","calls received\nmissed calls\nqueue\n")
page = page.replace("\n00:00:00\n","\n")
page += "\n" #
# regexp with groups to replace \n
page = re.sub(r'\n([0-9]{1,})\s([0-9]{1,})\s([0-9]{1,})\n', r'\n\1\n\2\n\3\n', page)
page = page[:-1] # remove last char \n
page = page.split("\n") # split a string by char \n (add array)
c2 = len(page) # find out the length of the array
for i in range(6, c2, 6): # adding json syntax to array
    jpage += "{\n \"" + page[0] + "\" : \"" + page[i] + "\",\n"
    jpage += "\"" + page[1] + "\" : \"" + page[i+1] + "\",\n"
    jpage += "\"" + page[2] + "\" : \"" + page[i+2] + "\",\n"
    jpage += "\"" + page[3] + "\" : \"" + page[i+3] + "\" ,\n"
    jpage += "\"" + page[4] + "\" : \"" + page[i+4] + "\",\n"
    jpage += "\"" + page[5] + "\" : \"" + page[i+5] + "\"\n},\n"
jpage = jpage[:-2] # removing extra char
jpage = "{\n\"Dashboard\" : [\n"+jpage+"]\n}" # adding json syntax to string
date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') # add date
file = open("dashboard-"+date+".json", "w") # add json file with date in name
file.write(jpage) # write json file
file.close() # close json file 
print("Completed "+date)