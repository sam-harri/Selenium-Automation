from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

loginID = '29003008330509'
AccountPIN = '647319'
pagenumberXPath = '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[5]/td/div[3]/div/div/div[2]/div[2]/span/a[2]'
addbuttonXPath = '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[5]/td/div[3]/div/div/table/tbody/tr[6]/td[9]/table/tbody/tr[1]/td/span/span/a'
path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://geegeereg.uottawa.ca/geegeereg/Start/start.asp')
driver.maximize_window()
wait = WebDriverWait(driver,100)


wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[5]/div[3]/div[2]/a'))).click() #login button
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/table/tbody/tr[1]/td[2]/input'))).send_keys(loginID) #inputs username
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/table/tbody/tr[2]/td[2]/input'))).send_keys(AccountPIN) #inputs password
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/table/tbody/tr[4]/td[1]/span/input'))).click() #login
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr/td[1]/a/span[2]'))).click() #register for program
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[3]/ul/li[4]/span/a'))).click() #Fitness and Wellness sub category
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[9]/td/div[3]/span[1]/a'))).click() #Workout seesion sub-sub category