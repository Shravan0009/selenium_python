
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://uat.pbees.party/en/parent")
driver.maximize_window()
time.sleep(10)
#driver.find_element(By,ID, "")
#driver.find_element(By.Name, "")
#driver.switch_to.alert.text("Read Now")

driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/a[7]/span/span/div/div[2]/a').click()
time.sleep(4)
try:
    alrt = driver.switch_to.alert.text("Read Now")
    print(alrt)

except NoSuchElementException as e:

    print("No alert found" ,e)

finally:
    # close the browser
    driver.quit()




    


print(alrt)

#driver.find_element()

#
#driver.quit()
