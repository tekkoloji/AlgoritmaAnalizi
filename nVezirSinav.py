def vezir(n):
    k=0
    dizi=[]
    for s in range(0,n):
        dizi.append(0)
    def forfonk(k):
        if(k==n):
            print dizi
            #uygunluk fonksiyonu
        else:
            k=k+1
            for i in range(1,n+1):
                dizi[k-1]=i
                forfonk(k)                
    forfonk(k)
    
vezir(4)
