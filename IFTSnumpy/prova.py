import numpy as np

a = np.array( [ 1, 2, 3 ] )
b = [ 1, 2, 3 ]
c = np.array( [ 1, 2, 3 ] )

print(a * 5)
print(b * 5)
print(a * c)
print(a + c)
print(a ** c)

r = np.arange(10)
print(r[2:8:3])
print(r[::-1])

r[3:5] = 99

print(r)

I = np.array( [ [1,2,3], [0,0,0], [3,2,1] ] )
print(len(I.shape), I.shape)

I[0:2 , 0:2] += 5
print(I[0:2 , 0:2])
print(I)

for row in I:
    for col in row:
        print(col)

for x in np.nditer(I):
    print(x)

for x in I.flatten():
    print(x)

for pos, x in np.ndenumerate(I):
    print(pos, x)
    i, j = pos # l'indice è una tupla poichè ho una matrice bidimensionale
    # x = 0
    # I[i, j] = 0

print(I.T)

F = I.copy()
for pos, x in np.ndenumerate(I):
    i, j = pos
    F[j, i] = x # x == I[i, j]
print(F)

I = np.arange(40000)
I = I.reshape(200, 200)

I = np.zeros_like(I).astype(np.uint8)
I[50:100, 50:100] = 100
I[:, 70:80] += 100
I[:100:5] += 100

import cv2

I = cv2.imread("botti.png").astype(np.int16)
print(I.shape)

I[:200,:, [0,2]] = 0

I[300:400, 300:400, 0] = 0
I[300:400, 300:400, 1] = 0
I[300:400, 300:400, 2] = 255

I[550:, 600:] = [50,0,150]

I[:,:,2] += 30

I //= 2
I += 128

I[I > 255] = 255

#cv2.imshow("I", (I.max(2).T).astype(np.uint8))
cv2.imshow("I", I.reshape(1202,-1, 3).astype(np.uint8))
cv2.waitKey(0)