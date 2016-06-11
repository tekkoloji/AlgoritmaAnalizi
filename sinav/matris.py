a=[[2,3],[4,5]]
b=[[1,4]]

for x in range(0,len(a)):
    list=a[x]
    for y in range(0,len(b[0])):
        toplam=0
        for z in range(0,len(list)):
            #print list[z]+" "+b[z][y]
            toplam=toplam+list[z]*b[z][y]
        print toplam,
    print " "
        
