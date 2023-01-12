import glob
import re
import cv2

gambarlist = glob.glob("*.jpg")

for i,gambar in enumerate(gambarlist):
	img = cv2.imread(gambar)
	data = gambar.split(".")
	timeStamp = data[4]
	typeV = data[5]
	plate = data[6]
	colour = data[7]
	cordinat = data[8]

	print(f"""
===============================
All Data Captured by TCM Camera
File No : {i+1},
Time : {timeStamp},
typeV : {typeV},
plate : {plate},
colour : {colour},
cordinat : {cordinat}
===============================""")
	s = str(cordinat)
	res = re.split("(\\d+)", s)

	x = res[1]
	y = res[3]
	w = res[5]
	h = res[7]

	cordinatR = [x,y,w,h]
	print("Cordinat : ", cordinatR)
	print("===============================")


	cv2.rectangle(img, (int(x),int(y)), (int(x)+int(w), int(y)+int(h)), (255,0,0), 4)
	status = cv2.imwrite(f"cobaimg/coba{i}.jpeg",img)
	print(status)

