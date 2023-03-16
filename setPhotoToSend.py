from waterMarkPhotos import *


def setPhotoToSend(flyer,config):


    if flyer == "yechi":
        basePhoto = "C:\\Users\\User\\Documents\\הודעות לגזברים\\allFlyers\\yechi\\" +config["flyerName"]
        photoToSend = waterMarkPhotos(basePhoto, config["last"], config["logoSize"] , config["logoPositionForYechi"], "", (0,0))
        
    elif flyer == "english":
        basePhoto = "C:\\Users\\User\\Documents\\הודעות לגזברים\\allFlyers\\english\\" +config["flyerName"]
        photoToSend = waterMarkPhotos(basePhoto, config["last"], config["logoSize"] , config["logoPositionForAnti"], "", (0,0))

    elif flyer == "french":
        basePhoto = "C:\\Users\\User\\Documents\\הודעות לגזברים\\allFlyers\\french\\" +config["flyerName"]
        photoToSend = waterMarkPhotos(basePhoto, config["last"], config["logoSize"] , config["logoPositionForAnti"], "", (0,0))
    
    else:
        basePhoto = "C:\\Users\\User\\Documents\\הודעות לגזברים\\allFlyers\\anti\\" + config["flyerName"] 
        photoToSend = waterMarkPhotos(basePhoto, config["last"], config["logoSize"], config["logoPositionForAnti"], "", (0,0))

    return photoToSend
