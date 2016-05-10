

def SiraliArama(aranan,dizi):
    k=0
    for i in dizi:
        k=k+1
        if(aranan==i):
            return ("aradiginiz %s degeri %s .sirada bulundu"%(aranan,k))


dizi=[1,2,3,4,5,6,7,8,9,10]

aranan=int(raw_input("Aradigin sayiyi gir :"))

print SiraliArama(aranan,dizi)
