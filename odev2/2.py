dosya=open("tablo1.txt", "r")
#headerlar baslik dizisi icerisinde
baslik=dosya.readline().split(",")
#veriler veri icerisinde. her satir bir dizi elemani
veri=dosya.readlines(1)
boyut=len(baslik)

maks=0
for j in range(0,boyut-1):
    for i in range(j+1,boyut):
        curmaks=0
        for satir in veri:
            degerj=satir.split(",")[j].replace('\n','')
            degeri=satir.split(",")[i].replace('\n','')
            if(degerj=='1' and degeri=='1'):
                curmaks=curmaks+1

        if(curmaks>maks):
            maks=curmaks
            indisi=i
            indisj=j
        

print ("%s%s urunu %s kere satildi"%(baslik[indisj],baslik[indisi],maks))
