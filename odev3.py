import random

def maxSubSum2(array):
    maxSum1=0
    for i in range(0,len(array)):
        thisSum1=0
        for j in range(i,len(array)):
            thisSum1=thisSum1+array[j]
            if(thisSum1>maxSum1):
                maxSum1=thisSum1
    return maxSum1

def maxSubSum1(array):
    maxSum=0
    for i in range(0,len(array)):
        for j in range(i,len(array)):
            thisSum=0
            for k in range(i,j):
                thisSum=thisSum+array[k]
            if(thisSum>maxSum):
                maxSum=thisSum
    return maxSum

array=[4,-3,5,-2,-1,2,6,-2]
size=int(input("dizinin boyutu ne olsun"))
array1=[]
for i in range(0,size):
    array1.append(random.randint(-20,20))
    
print("dizinin boyutu : ",len(array1))
print("diznin elemanları : ")
for i in range(0,size):
    print(i,".   ",array1[i])
    
import time
start_time=time.time()
print("maxSubSum1 sonucu :", maxSubSum1(array1))
print("gecen süre : ", time.time()-start_time)
print("maxSubSum2 sonucu :", maxSubSum2(array1))
print("gecen süre : ", time.time()-start_time)