from toWhatsAppLink import *
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver




def sendFirstMsg(driver, tel, rec, config, last):
    # textMsgInput = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')       
    textMsgInput = WebDriverWait(driver, timeout = 15).until(
            lambda d: d.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')                                  
        )    
    
    time.sleep(0.5)


    # שליחת קישור עם הודעה מובנית
    if config["sendStartMSG"] == True:
        textMsgInput.send_keys(toWhatsAppLink(tel, rec[config["startMSG"]])) 
    else:
        textMsgInput.send_keys(toWhatsAppLink(tel, "")) 
    time.sleep(0.5)

    sendMsgButton = WebDriverWait(driver, timeout = 15).until(
            lambda d: d.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        )    
    # sendMsgButton = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    sendMsgButton.click()
    time.sleep(0.5)

    findLinkToMsg = driver.find_element(By.PARTIAL_LINK_TEXT, str(tel))
    findLinkToMsg.click()

    time.sleep(0.5)
    
        ###אם לא רוצים לצרף תמונה   
    if config["sendStartMSG"] == True:

        time.sleep(1.5)
        sendMsgButton = WebDriverWait(driver, timeout = 15).until(
            lambda d: d.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        )    

        sendMsgButton.click()
        print("*msg number " + str(last) + " sent to " + rec["name"][::-1] + " " + str(tel))

    


def addPhotoToMSG(driver, last, fileAttachment, captionWithAttachment):
    # sendPhotoButton = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span')
    # sendPhotoButton.click()
    
    attachFile = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')            
    attachFile.click()
    time.sleep(0.5)

    inputFile = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input')
    inputFile.send_keys(fileAttachment)   
    # time.sleep(0)
    
    if captionWithAttachment:
        # caption = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
        caption = WebDriverWait(driver, timeout = 5).until(
            # lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p')
            lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
        )                                       

        caption.send_keys(captionWithAttachment)
        time.sleep(0.5)
    
    sendPhotoButton = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span')
    sendPhotoButton.click()
    
    return print("*photo number " + str(last) + " sent !")


def sendMsgTextAfter(driver, config, rec):
    
    time.sleep(1)
    textMsgInput = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')  
    time.sleep(1)
    # textMsgInput.send_keys("0000")
    textMsgInput.send_keys(rec[config["msg1"]])
    time.sleep(0.5)
    textMsgInput.send_keys(Keys.RETURN)

    # inputFile = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    # inputFile.send_keys("hjh vnk vnahj")
    time.sleep(1)
    
    # sendMsgButton = WebDriverWait(driver, timeout = 2).until(
    #     lambda d: d.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')                                            
    # )  
    # sendMsgButton.click()