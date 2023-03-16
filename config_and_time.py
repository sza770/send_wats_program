from datetime import datetime

# לפני שבת 
config = {
    "sendMsgTo": "DAILY",
    # "sendMsgTo": "yes",
    "last": 4,

    "sendStartMSG": True, 
    "startMSG": "msg1",

    "attachPhotoToStartMSG": False,

    "sendflyer": True, 

    "sendAttachment": False, 
    'attachment': lambda n: "C:\\Users\\User\\Documents\\web dev\\videoLogoPaster\\VideoOutput\\orgVideo" + str(n-1) + ".mp4",

    #ההודעה שמתחת לפלאייר, תמונה או סרטון
    "sendMsgWithAttachment": True, 
    "msgWithAttachment": "link",

    "sendMsgAfterPhoto": False, 
    "msgAfterPhoto": "msg1",

    # "flyerName":"36.jpg",
    "flyerName":"shabasTimes.jpg",
    "english" :False,
    "french" : False,
    "logoSize": (210,210), # no more then (250,250)
    "logoPositionForAnti" : ("right", "bottom"), # may be ("left", "bottom") or ("right", "bottom")
    "logoPositionForYechi" : ("right", "bottom"),  # may be ("left", "bottom") or ("right", "bottom")
}


def printDateTime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("                                                                            date and time =", dt_string,)



#עבור שליחת סרטונים. יש לשנות לזה שם לקונפיג
for_sending_videos = {
    "sendMsgTo": "DAILY",
    # "sendMsgTo": "yes",
    "last": 0,

    "sendStartMSG": True, 
    "startMSG": "msg4",

    "attachPhotoToStartMSG": False,

    "sendflyer": False, 

    "sendAttachment": True, 
    'attachment': lambda n: "C:\\Users\\User\\Documents\\web dev\\videoLogoPaster\\VideoOutput\\orgVideo" + str(n-1) + ".mp4",

    "sendMsgWithAttachment": True, 
    "msgWithAttachment": "link",

    "sendMsgAfterPhoto": False, 
    "msgAfterPhoto": "msg1",

    # "flyerName":"36.jpg",
    "flyerName":"shabasTimes3.jpg",
    "english" :False,
    "french" : False,
    "logoSize": (210,210), # no more then (250,250)
    "logoPositionForAnti" : (15,750),
    "logoPositionForYechi" : (15,750),
}