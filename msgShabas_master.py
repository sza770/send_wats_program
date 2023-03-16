from selenium import webdriver
from recipines_master import *
from toWhatsAppLink import *
from sendFirstMsg import *
from setPhotoToSend import setPhotoToSend
from config_and_time import *
# from addPhotoToMSG import addPhotoToMSG
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import json

service = Service(executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

printDateTime()

#פלאייר בעל שם טוב - נשלח עד מספר 61


failed = []

driver.get("https://web.whatsapp.com/")

last = config["last"]

time.sleep(1)
inputSearch = WebDriverWait(driver, timeout = 60).until(
    lambda d: d.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
)

time.sleep(1)
print("Element is visible? " + str(inputSearch.is_displayed()))
inputSearch.send_keys("לעצמי")
time.sleep(0.5)
inputSearch.send_keys(Keys.ARROW_DOWN)
inputSearch.send_keys(Keys.RETURN)

for rec in recipines[last:len(recipines)+1]:
    
    last = config["last"]
    if rec["LEVEL"] != config["sendMsgTo"]:
        config["last"] = config["last"] + 1
        continue


    orgsTelefones = rec["tel"].split(",")

    for tel in orgsTelefones:
        
        try:
            
            sendFirstMsg(driver ,tel, rec, config, last)

            if config["sendflyer"] == True:
                
                baseFlyer = rec["flyer"].split(",")

                for fly in baseFlyer:
            
                    if fly == "french" and config["french"] == False:
                        continue
                    if fly == "english" and config["english"] == False:
                        continue
                    
                    caption = rec[config["msgWithAttachment"]] if config["sendMsgWithAttachment"] else ""
                    addPhotoToMSG(driver, config["last"] ,setPhotoToSend(fly, config), caption)
                    
                    if config["sendMsgAfterPhoto"] == True:
                        sendMsgTextAfter(driver, config, rec)   

            if config["sendAttachment"] == True:
                caption = rec[config["msgWithAttachment"]] if config["sendMsgWithAttachment"] else ""
                addPhotoToMSG(driver, config["last"] , config["attachment"](config["last"]) , caption)

                    

                #לעשות
                #להוסיף לינק להודעות באנגלית וצרפתית, בתוך הפונקציה ADDPHOTOTOMSG
               
        
        except:
            
            try:
                ok = WebDriverWait(driver, timeout = 3).until(
                    lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div')
                    )
                ok.click()
                print( "FAILED " + str(tel) +" "+ rec["name"][::-1])
            except: 

                print( "FAILED X2" + str(tel) +" "+ rec["name"][::-1])
                failed.append( str(tel) +" "+ rec["name"][::-1])
                print("failed again")

        finally:

            time.sleep(3)

            inputSearch = WebDriverWait(driver, timeout = 2).until(
                lambda d: d.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]')
            )

            inputSearch.send_keys(Keys.ARROW_DOWN)
            inputSearch.send_keys(Keys.RETURN)




            

    config["last"] = config["last"] + 1



print("done!!!")
print("done!!!")
print("done!!!")
print("done!!!")
print(failed)

driver.quit()



# _________________________________________
# לשלוח הודעות לאנשי קשר ידועים
# x = ["טלי", "טלי","לעצמי", "טלי"]
# for n in x:
#     findChat = WebDriverWait(driver, timeout = 60).until(
#         lambda d: d.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
#         )
#     findChat.send_keys(n)
#     findChat.send_keys(Keys.RETURN)

#     msgField = WebDriverWait(driver, timeout = 5).until(
#         lambda d: d.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
#         )
#     # msgField = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
#     msgField.send_keys("ניסיון" + n)
#     msgField.send_keys(Keys.RETURN)
# _________________________________________



#################################################

# להקליק
# send.click()

# לקבל את שם הדף
# driver.title

# לסגור את הטאב
# driver.close

# לסגור את הדפדפן
# driver.quit()

# למצוא אלמנט
# driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')





