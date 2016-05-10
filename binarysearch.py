def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        #ikiye bolme
        x = lower + (upper - lower) // 2
        deger = array[x]
        if hedef == deger:
            return x
        #ust aralik
        elif hedef > deger:
            if lower == x:
                break        
            lower = x
        #aralik
        elif hedef < deger:
            upper = x

print binary_search([1,5,8,10], 8)
