# This is a script to save the most recent Colonial invoice for each client.

# They will be saved in your downloads folder.
# You'll need to move them to the client folders.
# We can't save directly to the network because of permissions issues.
# You should run this once a month around the end of the month.

# Maintain the list of clients and BCNs as we add and remove clients.
# change the filepath to the path for your downloads folder


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import datetime
from datetime import date
import pandas as pd
import shutil
import os

BCNS = {'Queen': 'E1234567', 'LexCorp': 'E2345678', 'DailyPlanet': 'E3456789'}

filepath = 'C:\\Users\\YourUserName\\Downloads'

#if you run it at the end of the month - label them for due date of next month
today = date.today()
nextmo = today+datetime.timedelta(weeks=2)
yrmo = nextmo.strftime("%Y-%m")

cluser = input("Colonial user name: ")
clpwd = input("Colonial password: ")

driver = webdriver.Chrome("C:\Python\Chromedriver\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://my.coloniallife.com/producers/Account%20Billing")

#step 1 - log in to colonial life website

element = driver.find_element_by_id("LoginId")
element.send_keys(cluser)
element = driver.find_element_by_id("password")
element.send_keys(clpwd)
element.send_keys(Keys.RETURN)
time.sleep(10)

#step 2 - for each client, enter the BCN
for abbrev, bcn in BCNS.items():
    element = driver.find_element_by_id("BCN-input")
    element.send_keys(bcn)
    element.send_keys(Keys.RETURN)
    time.sleep(10)

    #step 3 - click the link to the most recent invoice - paid or unpaid
    ele4thunpaid = driver.find_elements_by_xpath("/html/body/form/div[5]/div/div/div/div/div[3]/div[3]/section[1]/ul/li[4]/div[2]")
    ele3rdunpaid = driver.find_elements_by_xpath("/html/body/form/div[5]/div/div/div/div/div[3]/div[3]/section[1]/ul/li[3]/div[2]")
    ele2ndunpaid = driver.find_elements_by_xpath("/html/body/form/div[5]/div/div/div/div/div[3]/div[3]/section[1]/ul/li[2]/div[2]")
    #note - 1st of multiple unpaid is /html/body/form/div[5]/div/div/div/div/div[3]/div[3]/section[1]/ul/li[1]/div[2], but if there are multiples we will want later one anyway
    ele1unpaid = driver.find_elements_by_xpath("/html/body/form/div[5]/div/div/div/div/div[3]/div[3]/section[1]/ul/li/div[2]")
    ele1sched1 = driver.find_elements_by_xpath("/html/body/form/div[5]/div/div/div/div/div[3]/div[3]/section[2]/ul/li/div[2]")
    #guessing on next 1 - payments in process - no examples right now
    ele1inproc = driver.find_elements_by_xpath("/html/body/form/div[5]/div/div/div/div/div[3]/div[3]/section[3]/ul/li/div[2]")
    ele1stpaid = driver.find_elements_by_xpath("/html/body/form/div[5]/div/div/div/div/div[3]/div[3]/section[5]/ul/li[1]/div[2]")

    if len(ele4thunpaid) > 0:
        ele4thunpaid[0].click()
    elif len(ele3rdunpaid) > 0:
        ele3rdunpaid[0].click()
    elif len(ele2ndunpaid) > 0:
        ele2ndunpaid[0].click()
    elif len(ele1unpaid) > 0:
        ele1unpaid[0].click()
    elif len(ele1sched1) > 0:
        ele1sched1[0].click()
        time.sleep(5)
        ele1sched2 = driver.find_elements_by_xpath("/html/body/form/div[5]/div/div/div/div/div[3]/div[3]/section[2]/ul/li/div[3]/ul/li/div[1]/a")
        ele1sched2[0].click()
    elif len(ele1inproc) > 0:
        ele1inproc[0].click()
    elif len(ele1stpaid) > 0:
        ele1stpaid[0].click()
    time.sleep(10)

    #save excel and rename
    element = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div/div/div[3]/div[2]/div[2]/section[2]/div/a[1]/span[1]")
    element.click()
    time.sleep(7)
    rptname = abbrev + "-colonial-" + yrmo + ".xlsx"
    filename = max([filepath + "\\" + f for f in os.listdir(filepath)],key=os.path.getctime)
    shutil.copy(filename,os.path.join(filepath,rptname))

    #save PDF and rename
    element = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div/div/div[3]/div[2]/div[2]/section[2]/div/a[2]/span[1]")
    element.click()
    time.sleep(7)
    rptname = abbrev + "-colonial-" + yrmo + ".pdf"
    filename = max([filepath + "\\" + f for f in os.listdir(filepath)],key=os.path.getctime)
    shutil.copy(filename,os.path.join(filepath,rptname))

    #go back twice to the page where we can enter the BCN of the next group
    driver.back()
    time.sleep(7)
    driver.back()
    time.sleep(7)


