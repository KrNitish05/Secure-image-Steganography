import cv2
import os
x=cv2.imread("input.png")
if x is None:
    print("Error:Could not read input image.")
    exit()

i=x.shape[0]
j=x.shape[1]

d= [chr(i)  for i in range(256)]

reverse_d = {i: chr(i) for i in range(256)}

n,m,z,k1 =0,0,0,0

key=input("Enter key to edit :")
text=input("Enter text to show :")
text_bytes= text.encode('utf-8')
for i in range(len(text_bytes)):
    x[n,m,z]=text_bytes[i]^ord(key[k1])
    n=(n+1)% x.shape[0]
    m=(m+1)% x.shape[1]
    k1=(k1+1)%len(key)
    
cv2.imwrite("encrypted_img.png",x)
os.startfile("encrypted_img.png")

x=cv2.imread("encrypted_img.png")
if x is None:
    print("Error: Could not read encrypted image.")
    exit()
key1=input("Re enter key to extract text :")

decrypt_bytes= bytearray()
n,m,z,k1 =0,0,0,0
if key ==key1 :
    for i in range(len(text_bytes)):
        decrypt_bytes.append(x[n,m,z]^ord(key[k1]))
        n=(n+1)% x.shape[0]
        m=(m+1)% x.shape[1]
        k1=(k1+1)%len(key)

    decrypted_text= decrypt_bytes.decode('utf-8')
    print("Entered text was :",decrypted_text)
else:
    print("key doesn't matched.")

    
