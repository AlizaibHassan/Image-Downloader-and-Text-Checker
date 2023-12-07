import urllib.request
import os
import pytesseract
import csv
import requests
from PIL import Image


def download_img(image_url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',} 
    request=urllib.request.Request(image_url,None,headers)
    response = urllib.request.urlopen(request)

    #install PIL package to convert the response into a PIL Image object to further save it (Alizaib Comments)
    image=Image.open(response)
    image.save(full_path)
    pass

filepath = 'input/urls.txt'
saveimg = 'saveimg/'
basedata=open(filepath).read()

f = open("result.csv","a",newline="")


with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       
       line = line.rstrip('\n')

       print(line)
       img_name = str(cnt)
       fullfileurl = os.path.join(saveimg, str(cnt)+".jpg")
       download_img(line,saveimg,img_name)
                  
       pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
       checkdata=pytesseract.image_to_string(fullfileurl)


        
       if checkdata.isspace():
          towrite = (line,"No")
          writer = csv.writer(f)
          writer.writerow(towrite)
          
       else:
          towrite = (line,"Yes")
          writer = csv.writer(f)
          writer.writerow(towrite)


       line = fp.readline()
       cnt += 1

f.close()