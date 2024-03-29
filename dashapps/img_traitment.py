import cv2
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import csv
#Calcul du masque d'un objet par soustraction 
def calcul_masque (image, gray_fond, seuil):
    gray_frame=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    (longueur, largeur) = np.shape(gray_fond)
    masque = np.zeros((longueur, largeur))
    for x in range (longueur):
        for y in range (largeur):
            if (abs(int(gray_frame[x][y])-int(gray_fond[x][y])))>seuil:
                masque[x][y]=255
    kernel=np.ones((5, 5), np.uint8)
    masque=cv2.erode(masque, kernel, iterations=3)
    return masque

#Calcul du centre de l'objet grâce à son masque
def calcul_centre (masque):
    moy_x=0
    moy_y=0
    nb=0
    (longueur, largeur) = np.shape(masque)
    for x in range (longueur):
        for y in range(largeur):
            if masque[x][y]!=0:
                nb+=1
                moy_x=((moy_x*(nb-1))+x)/nb
                moy_y=((moy_y*(nb-1))+y)/nb
    return (np.floor(moy_x),np.floor(moy_y))

#Converti une vidéo en tableau d'image au format png
def video_en_image(video):
    # Vérifier si la vidéo est ouverte
    if not video.isOpened():
        print("Erreur: Impossible d'ouvrir la vidéo.")
    total_frame=int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    for frame in range (total_frame):
        video.set(cv2.CAP_PROP_POS_FRAMES,frame)
        success,image=video.read()
        if success:
            cv2.imwrite(f'../cache/image_{frame}.png',image)
    return total_frame

#Fonction principal qui prend en paramètre une vidéo et la transforme en un tableau avec l'ensemble des centres de l'objet
def video_en_donne(video):
    total_frame=video_en_image(video=video)
    tab_donne=[]
    fond=cv2.imread("../cache/image_0.png")
    gray_fond = cv2.cvtColor(fond, cv2.COLOR_BGR2GRAY)
    for i in range (total_frame):
        image=cv2.imread(f"../cache/image_{i}.png")
        masque=calcul_masque(image=image,gray_fond=gray_fond,seuil=10)
        tab_donne.append((calcul_centre(masque=masque),i/(video.get(cv2.CAP_PROP_FPS))))
    return tab_donne