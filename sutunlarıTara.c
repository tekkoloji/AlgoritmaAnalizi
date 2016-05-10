#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int satir,i,j,sale,maxindis=0,maxsale=0;

int main(int argc, char *argv[])
{
    srand(time(NULL));
    printf("Satir sayisini giriniz: ");
    scanf("%d",&satir);
    int dizi[satir][100];
    for( i = 0; i < satir; i++ ) {
		for( j = 0; j < 100; j++ ) {
             dizi[i][j]=rand()%2;
//             printf("%d\n",rand());
        }
    }
    for(i=0;i<100;i++){
           sale=0;
           for(j=0;j<satir;j++){
                   if(dizi[j][i]==1){
                         sale++;
                   }            
           }
           if(sale>maxsale){
                            maxsale=sale;
                            maxindis=i;
           }
    }
    printf("en cok satis yapilan urun: %d\n ", maxindis);
    
  
  system("PAUSE");	
  return 0;
}