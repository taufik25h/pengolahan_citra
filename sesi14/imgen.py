import numpy as np
import imageio.v3 as i
import matplotlib.pyplot as plt

def det(key):
    a =key [0][0]
    b =key [0][1]
    c =key [1][0]
    d =key [1][1]
    return (a*d)-(b*c)==1
 
def enc(img,key,cho):
     if not det(key):
         return"Matrix's Invalid"
     
     if cho==1:
         a =key [0][0]
         b =key [0][1]
         c =key [1][0]
         d =key [1][1]
     elif cho==2:
         d =key [0][0]
         b =256-key [0][1]
         c =256-key [1][0]
         a =key [1][1]
         
     result=np.zeros_like(img)
     for j in range(0,img.shape[0]-1,2):
         for k in range(0,img.shape[1]):
             r1= ((img[j,k,0]* a)+(img[j+1,k,0]* c))%256
             r2= ((img[j,k,0]* b)+(img[j+1,k,0]* d))%256
             
             g1= ((img[j,k,1]* a)+(img[j+1,k,1]* c))%256
             g2= ((img[j,k,1]* b)+(img[j+1,k,1]* d))%256
             
             b1= ((img[j,k,2]* a)+(img[j+1,k,2]* c))%256
             b2= ((img[j,k,2]* b)+(img[j+1,k,2]* d))%256
             
             result[j,k,0]= r1
             result[j+1,k,0]= r2
             
             result[j,k,1]= g1
             result[j+1,k,1]= g2
             
             result[j,k,2]= b1
             result[j+1,k,2]= b2                          
     return result.astype(np.uint8)
 
img=i.imread("C:\\latihan\\jinping.jpg")
key=np.array([
    [5,3],
    [3,2]
])

imgEnc = enc(img,key,1)
imgDec = enc(imgEnc,key,2)
plt.figure(figsize=(10,10))
plt.subplot(1,3,1)
plt.imshow(img)
plt.subplot(1,3,2)
plt.imshow(imgEnc)
plt.subplot(1,3,3)
plt.imshow(imgDec)

plt.show()
