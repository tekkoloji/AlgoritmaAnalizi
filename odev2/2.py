import itertools

dosya=open("tablo1.txt", "r")
#headerlar baslik dizisi icerisinde
baslik=dosya.readline().split(",")
#veriler veri icerisinde. her satir bir dizi elemani
veri=dosya.readlines(1)
boyut=len(baslik)

for adet in range(1,boyut+1):
    komb=list(itertools.combinations(range(0,boyut), adet))
    maks=0
    for eleman in komb:
        curmaks=0
        for satir in veri:
            durum=1
            for indis in eleman:
                deger=satir.split(",")[indis].replace('\n','')
                if(deger=='0'):
                    durum=0
            if durum==1:
                curmaks=curmaks+1

        if(curmaks>maks):
            maks=curmaks
            indisler=eleman


    urun=""
    for i in indisler:
        urun=urun+baslik[i].replace('\n','')

    print("------- %s karsilastirma ------"%adet)
    if(maks==0):
        print ("%s adet urun icin maks bulunamadi"%adet)
    else:
        print ("%s urunleri %s kere satildi"%(urun,maks))
    print("")
    

            


        


