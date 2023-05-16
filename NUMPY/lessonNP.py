# L'estensione del file .ipynb permette di organizzare il codice in celle

import numpy as np

a = np.array([1, 2, 3])  # questo li considera numeri
b = [1, 2, 3]  # questo lo considera un'array e moltiplica per 3 gli indici
c = np.array([1, 2, 3])


print(a * 5)
print(b * 3)
print(a * c)
print(c * b)
print(a + c)
print(a**c)
print("----------------------------------")

r = np.arange(10)  # crea un array di 10
print(r[2:8:3])
print(r[::-1])
r[3:7] = 99
print(r)
print("----------------------------------")
I = np.array([[1, 2, 3], [0, 0, 0], [3, 2, 1]])
print(len(I.shape), I.shape)
I[0:2, 0:2] += 5
print(I[0:2, 0:2])  # sottomatrice della matrice di partenza
print(I)


print("----------------------------------")
for row in I:
    for col in row:
        print(col)
print("----------------------------------")
for x in np.nditer(I):  # itera
    print(x)

for x in I.flatten():  # appiattisce
    print(x)

for pos, x in np.ndenumerate(I):
    print(pos, x)
    i, j = pos  # l'indice è una tupla poichè ho una matrice bidimensionale
    # x =0
    # I[i,j]=0  reset matrice
print("--------------------------------")
# Trasposizione di immagine
print("Matrice trasposta")
F = I.copy()  # creo una copia
for pos, x in np.ndenumerate(I):
    i, j = pos
    F[j, i] = x  # x = I[i,j]

    print(F)

    # Creare un'immagine

I = np.arange(
    40000
)  # array monodimensionale, quindi uso una funzione che si chiama reshape()
I = I.reshape((200, 200))

I = np.zeros_like(I).astype(
    np.uint8  # 8 bit
)  # crea un array con le stesse dimensioni, ma tutto fatto con gli 0
I[
    50:100, 50:100
] = 100  # scrivo in alcune righe e alcune colonne un valore numerico che crea colore
I[:, 70:80] += 100
I[:100:5] += 100

import cv2

I = cv2.imread("imagea.jpg")  # funzione per leggere le immagini
print(I.shape)  # shape proprietà per dare la forma

# I[
#     :, :, 1:2
# ] = 0  # i tre parametri sono i 3 colori primari RGB   si può usare lo slice tipo 2:1 per creare altri colori

I[:200, :, [0, 2]] = 0


I[300:400, 300:400, 0] = 0
I[300:400, 300:400, 1] = 0
I[300:400, 300:400, 2] = 255

I[550:, 600:] = [50, 0, 150]

I[:, :, 2] += 30

I //= 2
I += 128

I[I > 255] = 255

# cv2.imshow("Preview", (I.mean(2).T).astype(np.uint8)) #mean ovvero  la media oppure max o altre funzioni
# cv2.imshow("Preview", I.reshape(1202, -1, 3).astype(np.uint8))
cv2.imshow("Preview", (I.mean(2).T).astype(np.uint8))
cv2.waitKey(0)
