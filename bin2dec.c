#include<stdio.h>
#include<math.h>
int main()
{
int bin,bint, dec=0, lt,m,i;
printf("\nPlease Enter The Binary number : ");
scanf("%d",&bint);
bin = bint;
lt = log10(bin);
for(i = 0 ; i <= lt ; i++)
{
m = (bin % 10) ;
dec=dec+(m*pow(2,i));
bin=bin / 10;
}
printf("Decimal form of %d is %d\n",bint,dec);
return 0;
}
