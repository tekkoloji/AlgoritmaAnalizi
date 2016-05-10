def bubbleSort(dizi):
    boyut=len(dizi)
    for turSayisi in range(boyut-1,0,-1):
        for i in range(turSayisi):
            if dizi[i]>dizi[i+1]:
                temp = dizi[i]
                dizi[i] = dizi[i+1]
                dizi[i+1] = temp

dizi = [45,55,52,28,24,15,29,37,65]
bubbleSort(dizi)
print(dizi)
