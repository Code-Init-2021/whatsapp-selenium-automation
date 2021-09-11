from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
from pandas import read_csv

csv_data = read_csv('source.csv')
print(csv_data.head())
# Expects data in the format: phno, message
head, tail = csv_data.keys()

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  #chrome binary location specified here

options.set_capability("unhandledPromptBehavior", "accept")

driver = webdriver.Chrome(executable_path=r'C:\Users\heman\OneDrive\Desktop\Files\Projects\chromedriver.exe', options=options)
print("Driver loaded")

#Initial get to sign in to whatsapp via qr code
driver.get("https://web.whatsapp.com")
print("Waiting for login")
wait = WebDriverWait(driver, 60)
target='"root"'
x_arg = '//span[contains(@title,' + target + ')]'
wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
print("Login successful")

content = ""
prev = ""
for number, message in csv_data.values:
    if prev == "" or prev == number:
        content += str(message) + "\n"
        prev = number
    else:
        save = number
        number = str(prev)
        
        text = quote(head + content + tail)
        content = str(message) + "\n"
        if len(number) == 10:
            number = "+91" + number
        print("Sending message")
        print(text)
        print("To{}".format(number))
        print(f"https://web.whatsapp.com/send?phone={number}&text={text}")
        driver.get(f"https://web.whatsapp.com/send?phone={number}&text={text}")
        driver.implicitly_wait(20)

        driver.find_element_by_class_name('_4sWnG').click()
        prev = save
        number = save

number = str(prev)
        
text = quote(head + content + tail)
if len(number) == 10:
    number = "91" + number
print("Sending message")
print(text)
print("To{}".format(number))
print(f"https://web.whatsapp.com/send?phone={number}&text={text}")

driver.get(f"https://web.whatsapp.com/send?phone={number}&text={text}")
driver.implicitly_wait(20)

driver.find_element_by_class_name('_4sWnG').click()