import numpy as np# image  to array
from PIL import Image#image read
img=Image.open('moon.jpg')
a=np.array(img).reshape(-1,1)
print(a)
print("------------------------------------\n")
s=np.array([[1,2,3],[4,5,6]])
print(s)# rows=2 ,columns =3
print("------------------------------------\n")
t=s.reshape(3,2)
print(t)# row=3,columns=2  2d array
print("------------------------------------\n")
d=s.reshape(-1,1)
print(d) # 1d array
print("-------------")