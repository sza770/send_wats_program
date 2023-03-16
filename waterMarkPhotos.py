from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageFont
from PIL import ImageDraw


def waterMarkPhotos(    basePhoto,
                        n,
                        size = (250, 250),
                        imagePosition = (0,0) ,
                        text = "",
                        textPosition = (0,0),
                        saveTo="flyerOutput"
                    ):
    try:
        image = Image.open(basePhoto)
        copied_image = image.copy()
        
        if imagePosition == ("left","bottom"):
            height = image.height
            width = image.width
            imagePosition = (15, height-50 - size[0])

        if imagePosition == ("right","bottom"):
            height = image.height
            width = image.width
            imagePosition = (width- 30 - size[1], height-50 - size[0])

        #check if need to add text
        if text != "" :
            draw = ImageDraw.Draw(copied_image)
            font = ImageFont.truetype("calibri.ttf", 12)
            
            # add watermark text
            draw.text(textPosition, text[::-1], 
                    (0, 0, 0), font=font)

        logo = Image.open("C:\\Users\\User\\Documents\\הודעות לגזברים\\orgDATA\\logos\\logo" +  str(n - 1) + ".png") 
        crop_logo = logo.copy()

        crop_logo.thumbnail(size)

        # add watermark
        # copied_image = image.copy()
        copied_image.paste(crop_logo, imagePosition)
        
        copied_image.save("C:\\Users\\User\\Documents\\הודעות לגזברים\\send_wats_program\\" + str(saveTo) + "\\flyer" + str(n) + ".png")
        # copied_image.show()

        print(n, "photo complited")

        return "C:\\Users\\User\\Documents\\הודעות לגזברים\\send_wats_program\\flyerOutput\\flyer" + str(n) + ".png"
    except:
        print("can't create waterMark photo")


# # ליצירה ידנית  
def singlePhoto(last,baseNumber):
    basePhoto = "C:\\Users\\User\\Documents\\הודעות לגזברים\\allFlyers\\anti\\"+ str(baseNumber) +".jpg"
    # basePhoto = "C:\\Users\\User\\Documents\\הודעות לגזברים\\allFlyers\\yechi\\"+ str(baseNumber) +".jpg"
    # waterMarkPhotos(basePhoto, last,(220,220), (15,750), saveTo="SingleFlyerOutput")
    waterMarkPhotos(basePhoto, last,(220,220), ("left","bottom"), saveTo="SingleFlyerOutput")

singlePhoto(190,"shabasTimes")

def newOrgFlyer(last):
    basePhoto = "C:\\Users\\User\\Documents\\הודעות לגזברים\\allFlyers\\anti\\new.jpg"
    # basePhoto = "C:\\Users\\User\\Documents\\הודעות לגזברים\\allFlyers\\yechi\\new.jpg"
    waterMarkPhotos(basePhoto, last,(340,340), (285,305), saveTo="SingleFlyerOutput")

# newOrgFlyer(206)


# C:\Users\User\Documents\הודעות לגזברים\send_wats_program\SingleFlyerOutput