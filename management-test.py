from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import subprocess
import time
import os

driver = webdriver.Chrome()

# Reset ulang database
def reset_database():

    # Menentukan alamat direktori yang ingin dikunjungi
    project_path = '/Users/ifanmuhammad/demo-app-cypress-automation'
    
    # Menggunakan modul os untuk berpindah direktori 
    os.chdir(project_path)
    
    # Menjalankan perintah artisan dengan memanfaatkan modul subprocess yang seperti dilakukan di terminal atau command prompt
    # capture untuk menangkap value bernilai true atau false 
    # text untuk mengembalikan value bernilai string
    result = subprocess.run(['php', 'artisan', 'migrate:fresh', '--seed'], capture_output=True, text=True)
    
    # result output berhasil
    print(result.stdout)

    # result output error
    print(result.stderr)

reset_database()

try:

    #Login Positive or Negative Test Case
    driver.get('http://127.0.0.1:8000/')
    driver.find_element(By.XPATH, '//*[@id="app"]/section/div/div/div/div[2]/div[2]/form/div[1]/input').send_keys('superadmin@gmail.com')
    driver.find_element(By.CSS_SELECTOR, '#app > section > div > div > div > div.card.card-primary > div.card-body > form > div:nth-child(3) > input').send_keys('password')
    driver.find_element(By.XPATH, '//*[@id="app"]/section/div/div/div/div[2]/div[2]/form/div[3]/button').click()

    #Dashboard
    time.sleep(3)
    hover_element = driver.find_element(By.XPATH, '//*[@id="sidebar-wrapper"]/ul/li[2]/a')
    actions = ActionChains(driver)
    actions.move_to_element(hover_element).perform()
    driver.find_element(By.XPATH, '//*[@id="sidebar-wrapper"]/ul/li[2]/ul/li/a').click()

    #Added User Positif or Negative Test Case
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/section/div[2]/div[2]/div/div/div[1]/div/a[1]').click()
    driver.find_element(By.ID, 'name').send_keys('Akun Coba')
    emailField = driver.find_element(By.ID, 'email')
    emailField.clear()
    emailField.send_keys('akuncoba@gmail.com')
    passwordField = driver.find_element(By.ID, 'password')
    passwordField.clear()
    passwordField.send_keys('akuncoba1234')

    # Button Cancel
    # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/section/div[2]/div/div[3]/a').click()
    time.sleep(3)
    # Button Submit
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/section/div[2]/div/div[3]/button').click()
    time.sleep(2)



    #Edited Positif or Negative User Test Case
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/section/div[2]/div[2]/div/div/div[2]/div[3]/table/tbody/tr[4]/td[5]/div/a').click()
    editedName = driver.find_element(By.ID, 'name')
    editedName.clear()
    editedName.send_keys('Akun Percobaan 1')

    editedEmail = driver.find_element(By.ID, 'email')
    editedEmail.clear()
    editedEmail.send_keys('akunpercobaan1@gmail.com')

    # Button Cancel
    # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/section/div[2]/div/form/div[3]/a').click()
    time.sleep(3)
    # Button Submit
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/section/div[2]/div/form/div[3]/button').click()
    time.sleep(2)



    #Deleted Account User Test Case
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/section/div[2]/div[2]/div/div/div[2]/div[3]/table/tbody/tr[4]/td[5]/div/form/button').click()

    # Button Cancel
    # driver.find_element(By.CSS_SELECTOR, 'body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div:nth-child(1) > button').click()

    # Button Deleted
    driver.find_element(By.CSS_SELECTOR, 'body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div:nth-child(2) > button').click()

finally: 
    time.sleep(5)
    reset_database()
    driver.quit()