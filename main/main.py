from PIL import Image
from numpy import asarray
import numpy as np
import sys
#barcode part
import os
import io
import pyqrcode
#threading part
import threading
import zlib

#loading the digital Image
image=Image.open('/home/darkhand/Documents/github/Image-to-Qrcode-Generator/src/dhoni.jpg')
#converting image to array


Matrix=np.asarray(image)

#recording the shape of the array
shape=Matrix.shape
#flattening the array to about 1d
np.set_printoptions(threshold=sys.maxsize)
flat_array=Matrix.flatten()

b=zlib.compress(flat_array,3)

print(b)

print(sys.getsizeof(b))
decompressed_data = zlib.decompress(b)
print(sys.getsizeof(decompressed_data))
print(flat_array.size)
#starting the qrcode func
class Qrcode(object):
    def __init__(self,text):
        self.qr_image=self.qr_generator(text)
    @staticmethod
    def qr_generator(text):
        qr_code=pyqrcode.create(text)
        file_name='Qrcode genrated'
        save_path=os.path.join(os.path.expanduser('~'),'Desktop')
        name=f"{save_path}{file_name}.png"
        qr_code.png(name,scale=10)
        image=Image.open(name)
        image=image.resize((400,400),Image.ANTIALIAS)
        image.show()

class Processor(threading.Thread):
    def __init__(self,array,n):
        threading.Thread.__init__(self)
        self.array=array
        self.n=n
        self.counter=0

    def run(self):
        self.counter=self.counter+1
        print("processing thread :",self.counter)


#Qrcode(str(flat_array))

#Qrcode(strings)
#reforming the array back to the original shape
#Matrix2=np.asarray(flat_array).reshape(shape)



#convert back array to image
#extracted_image=Image.fromarray(Matrix2)
#extracted_image.show()



