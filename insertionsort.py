def insertionSort(dizi):
    boyut=len(dizi)
    for index in range(1,boyut):
        simdikideger = dizi[index]
        pozisyon = index
        while pozisyon>0 and dizi[pozisyon-1]>simdikideger:
            dizi[pozisyon]=dizi[pozisyon-1]
            pozisyon = pozisyon-1
        dizi[pozisyon]=simdikideger

dizi = [12,25,23,45,85,27,85,96]
insertionSort(dizi)
print(dizi)
