from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

'''
driver.get("https://google.com")
# eleman görünene kadar maksimum 4 saniye bekle
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "q")))

# Google search bar ı bulmak (Full xpath yöntemi kullanılabilir)
# input_element_by_id = driver.find_element(By.ID, "APjFqb")
input_element_by_name = driver.find_element(By.NAME, "q")
# input_element_by_x_path = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
# print(input_element_by_id)
# print(input_element_by_name)
# print(input_element_by_x_path)

input_element_by_name.send_keys("adem alperen arda")

search_button = driver.find_element(By.NAME, "btnK")
WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "btnK")))
search_button.click()

'''

driver.get("https://atilsamancioglu.com")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")))
blog_page = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")
blog_page.click()

# DOMAIN DE KULLANILACAK
# WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button")))
# read_buttons = driver.find_elements(By.CLASS_NAME, "button")
# for button in read_buttons:
#    print(button)

read_button = driver.find_element(By.CLASS_NAME, "button")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button")))
read_button.click()

# DOMAIN DE KULLANILACAKKKK
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/aside[4]")))
article_list = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/aside[4]")
splitted_lines = article_list.text.splitlines()

print(f"atilsamancioglu.com has {len(splitted_lines)} blog posts")

while True:
    continue
