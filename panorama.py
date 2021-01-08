import cv2
import os

mainfolder='images'

folders=os.listdir(mainfolder)
print(folders)

print(type(folders))
images=[]
for img in folders:
    myimg=cv2.imread(f'{mainfolder}/{img}')
    myimg=cv2.resize(myimg,(0,0),None,0.2,0.2)
    images.append(myimg)


stitcher=cv2.Stitcher_create()
(status,result)=stitcher.stitch(images)

if status==(cv2.STITCHER_OK):
    print("Panorama created")
    cv2.imshow("result",result)
    cv2.waitKey(0)
else:
    print("Panorama not created")



