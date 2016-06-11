def eleman_ekle(h,k,v):
    indis = hash(k)%100
    eslesme = False

    for eleman in h[indis]:
        if k == eleman[0]:
            eleman[1] = v 
            eslesme = True

    if not eslesme:
        h[indis].append([k,v])

    return h
     
def bul(h,k):
    indis = hash(k)%100

    for eleman in h[indis]:
        if k == eleman[0]:
            return eleman[1]

    return 0

def main():
    hash_listesi = range(100)
    hash_listesi = [[] for i in hash_listesi]
    # print hash_listesi
    gorev = "e"

    while gorev.lower() == 'e':
        anahtar = raw_input("anahtar: ")
        deger = raw_input("deger: ")
        gorev = raw_input("Eleman eklemek ister misiniz? ('e' or 'h') ")

        hash_listesi = eleman_ekle(hash_listesi,anahtar,deger)
        print hash_listesi

    aranacak = raw_input("Aranan deger: ")
    aranan = bul(hash_listesi,aranacak)
    
    print aranan
    # print hash_listesi


main()
