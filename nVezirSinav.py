def vezir(n):
    k=0
    dizi=[0,0,0,0]
    def forfonk(k):
        if(k==n):
            print dizi
            #uygunluk fonksiyonu yazilacak
        else:
            k=k+1
            for i in range(1,n+1):
                dizi[k-1]=i
                forfonk(k)
                
    forfonk(k)
    

vezir(4)
