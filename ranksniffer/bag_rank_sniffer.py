import csv
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Driver setup
s = Service("C:\Program Files (x86)\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options,service=s)

#BUSD search filter
driver.get('https://www.binance.com/en/nft/collection/Badass-Ape-Guild?currency=BUSD&amountFrom=700&amountTo=3000&orderBy=amount_sort&orderType=1&isBack=1&id=520838987141468161&order=amount_sort%401')
#Get pass the Agreement & cookie wall:
WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[3]/div/div[1]/div/div[2]/div/button[2]"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept']"))).click()

print ("""
  ____            _                     _                   ____       _ _     _ 
 | __ )  __ _  __| | __ _ ___ ___      / \   _ __   ___    / ___|_   _(_) | __| |
 |  _ \ / _` |/ _` |/ _` / __/ __|    / _ \ | '_ \ / _ \  | |  _| | | | | |/ _` |
 | |_) | (_| | (_| | (_| \__ \__ \   / ___ \| |_) |  __/  | |_| | |_| | | | (_| |
 |____/ \__,_|\__,_|\__,_|___/___/  /_/   \_\ .__/ \___|   \____|\__,_|_|_|\__,_|
                                           |_|                                 """)
print ("""
  ____             _                  _  __  __           
 |  _ \ __ _ _ __ | | __    ___ _ __ (_)/ _|/ _| ___ _ __ 
 | |_) / _` | '_ \| |/ /   / __| '_ \| | |_| |_ / _ \ '__|
 |  _ < (_| | | | |   <    \__ \ | | | |  _|  _|  __/ |   
 |_| \_\__,_|_| |_|_|\_\   |___/_| |_|_|_| |_|  \___|_|   
                                                                         Made by @b41ss: https://twitter.com/b41ss""")
print ("**************************************************")
print ("Please wait.... do NOT close down the browser :)")
print ("The script opens up a Chrome browser and work it's magic > It will close automatically.")
print ("The output is created in a text file: id+rank.txt")
print ("The highest ranked Apes for sale are shown first.")
print ("Buy your favorite ranked Badass Ape, enter the ID in the searchbar on Binance NFT: https://bit.ly/3IL5tV7")
print ("AGAIN: Please wait until the automated chrome browser closes, than the text file is created ! :)")
print ("If the browser closes, and nothing happens press Enter.")
print ("**************************************************")

SCROLL_PAUSE_TIME = 10
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(1)
#Main logic
main = driver.find_elements(By.CSS_SELECTOR, "div.css-z6gv93")

file=open("ape_IDs.txt","w")

for m in main:
    print(m.text, file=open("ape_IDs.txt", "a"))

f = open("ape_IDs.txt")
lines = f.readlines()
f.close()
#Continue from here:

# Open a new window
driver.execute_script("window.open('');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
#ETH search filter
driver.get('https://www.binance.com/en/nft/collection/Badass-Ape-Guild?currency=ETH&amountFrom=0.2&amountTo=2&orderBy=amount_sort&orderType=1&isBack=1&id=520838987141468161&order=amount_sort%401')
SCROLL_PAUSE_TIME = 4

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(1)
    if new_height == last_height:
        break
    last_height = new_height

#Main logic
main = driver.find_elements(By.CSS_SELECTOR, "div.css-z6gv93")

file=open("ape_IDs.txt","a")

for m in main:
    print(m.text, file=open("ape_IDs.txt", "a"))

f = open("ape_IDs.txt")
lines = f.readlines()
f.close()

# Open a new window
driver.execute_script("window.open('');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[2])
driver.get('https://www.binance.com/en/nft/collection/Badass-Ape-Guild?currency=BUSD&amountFrom=600&amountTo=4000&orderBy=amount_sort&orderType=-1&isBack=1&id=520838987141468161&order=amount_sort%40-1')
#BUSD reversed filter

SCROLL_PAUSE_TIME = 4

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(1)
    if new_height == last_height:
        break
    last_height = new_height

#Main logic
main = driver.find_elements(By.CSS_SELECTOR, "div.css-z6gv93")

file=open("ape_IDs.txt","a")

for m in main:
    print(m.text, file=open("ape_IDs.txt", "a"))

f = open("ape_IDs.txt")
lines = f.readlines()
f.close()
f = open("ape_IDs.txt", 'w+')

#delete strings + #, so only integers/ID is left over.
for line in lines:
        f.write(line[12:])
f.close()
driver.quit()

time.sleep(2) # hereafter the second phase starts:

#get text file and convert to list:
with open("ape_IDs.txt") as f:
    content = [x for x in f.read().split()]

# Open ranking sheet and convert to list with string value (id) and integer Rank
with open('ranking_sheet_strings.csv') as f:
    rankings = list(csv.reader(f))      # Read all rows into a list

for row in rankings[1:]:    # Skip the header row and convert values to integers
    row[1] = int(row[1])

# Get ID + ranking, still need to sort on highest rank:
new = [i for e in content for i in rankings if e in i]

# sort highest ranked and delete duplicates:
def sortSecond(val):
    return val[1]
new.sort(key = sortSecond)
new_sorted = [i for j, i in enumerate(new) if i not in new[:j]]

with open('ID+rank.txt', 'w') as file:
    file.write('\n'.join(str(rank) for rank in new_sorted))
    print ("It's DONE, a text file named: id+rank.txt is created, open it to see what ranked Apes are for sale!")
