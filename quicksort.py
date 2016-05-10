def quick_sort(dizi,sol,sag):
    #sol pivot siniri
    #sag pivot siniri
    if sag-sol==1: return dizi
    i,j=sol,sag
    pivot=dizi[(sol+sag)/2]

    while i<j:
        while dizi[i]<pivot:i+=1
        while dizi[j]>pivot:j-=1
        dizi[i],dizi[j]=dizi[j],dizi[i]

    if sol<j:quick_sort(dizi,sol,j)
    if sag>i:quick_sort(dizi,i,sag)
    return dizi

print quick_sort([21,54,23,65,782,26,89],0,6)
